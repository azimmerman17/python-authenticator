from flask import request
from markupsafe import escape
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_jwt
from ua_parser import parse_os, parse_device, parse

from app.auth import bp
from app.auth.functions import generate_salt, hash_value, encrypt_data
from app.auth.queries import validate_user, get_person
from app.functions.sql_functions import run_query
from app.models.person import Person
from config import Config

# Authenicate a user for log in
# @bp.route('/login', methods=['POST'])

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
      person_id = run_query('SELECT LAST_INSERT_ID()', hide=False).mappings().all()
    except Exception as error:
      print(error)
      return {'msg': 'Error inserting new user data'}, 500

    # retrieve the person id and Create JWT token for user
    try:
      id = run_query('SELECT LAST_INSERT_ID() AS "id"', hide=False).mappings().all()
      person_id = id[0]['id']
      
      access_token = create_access_token(identity=person_id)
      person = Person(person_id=person_id, user_name=data['user_name'], first_name=data['first_name'], last_name=data['last_name'], email=data['email']).as_dict()
    except Exception as error:
      print(error)
      return {'msg': 'User created, error logging user in - Please attempt to log in'}, 500

    # Send a welcome email - Future Work
    # email = welcome_email(data, config_class)
    # send_email(email, config_class)

    return {'msg': 'Account Created', 'access_token': access_token, 'person': person}, 200








# JWT protected route for to get a logged in user
# @bp.route('/user', methods=['POST'])
# @jwt_required()
 