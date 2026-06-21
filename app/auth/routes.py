from flask import request
from markupsafe import escape
from datetime import datetime, timedelta
import jwt

from app.auth import bp
from app.auth.functions import generate_salt, hash_value, encrypt_data, authenicate_user
from app.auth.queries import validate_user, get_person
from app.email.welcome_email.html import welcome_email
from app.email.functions import send_email
from app.functions.sql_functions import run_query
from app.models.person import Person
from config import Config

# Authenicate a user for log in
@bp.route('/login', methods=['POST'])
def user_login(config_class=Config):
  if request.method == 'POST':
    data = request.json

    # authenticate user to get the person
    person = authenicate_user(data['user_name'], data['password'], config_class)

    if person == 'Error':
      return {'message': 'Unable to authenticate user based on username/email and password combination'}, 401
    
    # create JWT access token
    token_expires = datetime.now() + Config.JWT_ACCESS_TOKEN_EXPIRES
    if isinstance(token_expires, (datetime)):
      token_expires =  token_expires.isoformat()
    # access_token = create_access_token(identity=person['person_id'])
    access_token = jwt.encode({"person": person, 'token_expires': token_expires}, Config.JWT_SECRET, algorithm=Config.JWT_ALGORITHM)
    return {'message': 'Login Success', 'access_token': access_token, 'person': person}

# Create new user
@bp.route('/new', methods=['POST'])
def new_user(config_class=Config):
    data = request.json
    # inputs -- first_name, last_name, user_name, email, password, app
    # auto-generate -- user_id,, created_at, update_at, reset_token_expires
    # dervived -- salt, password_hash, reset_token

    # validate user_name, email, password are present
    if data['user_name'] is None or data['email'] is None or data['password'] is None or data['first_name'] is None or data['last_name'] is None:
      return  {'msg': 'Unable to create user, required fields are missing.'}, 400

    # Validate if user_name and email are unique
    validate_new = validate_user(data['user_name'], data['email'])
    try:
      v = run_query(validate_new, hide=False).mappings().all()
      if len(v) > 0:
        return {'msg': 'Username or email already exists'}, 400
    except Exception as error:
      print(error)
      return {'msg': 'Error validating new user'}, 500

    # Build dervived user information
    salt = generate_salt()                                                                # user salt
    encrypted_salt = encrypt_data(salt, config_class).decode()                            # encrypt salt
    password_hash = hash_value(data['password'] + salt.decode()) + config_class.PEPPER    # hash password
    reset = hash_value(generate_salt().decode())                                          # reset token

    insert_query = Person(user_name=data['user_name'], first_name=data['first_name'], last_name=data['last_name'], email=data['email'], salt=encrypted_salt, password_hash=password_hash, reset_token=reset).person_insert()

    try:
      run_query(insert_query, hide=False)
    except Exception as error:
      print(error)
      return {'msg': 'Error inserting new user data'}, 500

    # retrieve the person id and Create JWT token for user
    try:
      id = run_query('SELECT LAST_INSERT_ID() AS "id"', hide=False).mappings().all()
      person_id = id[0]['id']

      person = Person(person_id=person_id, user_name=data['user_name'], first_name=data['first_name'], last_name=data['last_name'], email=data['email']).as_dict()
      token_expire = datetime.now() + Config.JWT_ACCESS_TOKEN_EXPIRES
      if isinstance(token_expire, (datetime)):
        token_expire =  token_expire.isoformat()
      access_token = jwt.encode({'person': person, 'token_expires': token_expire}, Config.JWT_SECRET, algorithm=Config.JWT_ALGORITHM)
    except Exception as error:
      print(error)
      return {'msg': 'User created, error logging user in - Please attempt to log in'}, 500

    # Send a welcome email
    email_html = welcome_email(person, data['app'])
    payload = {
      'subject': f'Welcome to {data['app']['company']}',
      'from': config_class.MAIL_USERNAME,
      'to': data['email'] if config_class.ENV == 'PROD' else config_class.MAIL_USERNAME,
      'html': email_html
    }
    
    send_email(payload, config_class)

    return {'msg': 'Account Created', 'access_token': access_token, 'person': person}, 200

# JWT protected route for to get a logged in user
@bp.route('/user', methods=['POST'])
def get_user(config_class=Config):
  if request.method == 'POST':
    try:
      token = request.headers['Authorization'].split(' ')[1]

      # decode token
      decoded_token = jwt.decode(token, Config.JWT_SECRET, algorithms=[Config.JWT_ALGORITHM])
      # check if expired -- reissue new token if not expires
      if datetime.now().isoformat() <= decoded_token['token_expires']:
        person = decoded_token['person']
        new_expire = datetime.now() + Config.JWT_ACCESS_TOKEN_EXPIRES
        if isinstance(new_expire, (datetime)):
          new_expire =  new_expire.isoformat()
        
        new_token = jwt.encode({'person': person, 'token_expires': new_expire}, Config.JWT_SECRET, algorithm=Config.JWT_ALGORITHM)
        return {'message': 'Success', 'access_token': new_token, 'person': person}
      else:
        return {'message': 'Token expired'}
    except Exception as error:
      print('ERROR', error)
      return {'msg': 'Unable to retrieve user'}, 500

# Update 
@bp.route('/update/<int:id>', methods=['PUT'])
def update_user(id, config_class=Config):
  data = request.json

  # retrieve and remove access token fron data
  access_token = data['access_token']
  del data['access_token']

  # update password
  if 'password' in data:
    # Build dervived user information
    salt = generate_salt()                                                                # user salt
    encrypted_salt = encrypt_data(salt, config_class).decode()                            # encrypt salt
    password_hash = hash_value(data['password'] + salt.decode()) + config_class.PEPPER    # hash password
    
    # build password query and remove password from data
    password_query = Person(person_id=id).update_password(password_hash, encrypted_salt)
    del data['password']

    # run password query
    try:
      run_query(password_query)
    except Exception as error:
      print('ERROR', error)
      return {'msg': 'Unable to update user password'}, 500

  # check if data has keys
  if data:
    person_query = Person(person_id=id).update_person(data)

    # run password query
    try:
      run_query(person_query)
    except Exception as error:
      print('ERROR', error)
      return {'msg': 'Unable to update user data'}, 500

    # update access token data
    decoded_token = jwt.decode(access_token, Config.JWT_SECRET, algorithms=[Config.JWT_ALGORITHM])
    person = decoded_token['person']
    
    for key in data:
      person[key] = data[key]

    new_token = jwt.encode({'person': person, 'token_expires': decoded_token['token_expires']}, Config.JWT_SECRET, algorithm=Config.JWT_ALGORITHM)
    
  return {'msg': 'User data updated', 'person': person, 'access_token': new_token}, 200
