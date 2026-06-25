from app.auth.queries import get_person_auth
from app.functions.sql_functions import run_query
from app.models.person import Person

# function to generate salt
def generate_salt():
  from cryptography.fernet import Fernet
  key = Fernet.generate_key()
  return key

# function to hash a value
def hash_value(value):
  from Crypto.Hash import SHA3_256

  # Calling createHash method
  hash_dict = SHA3_256.new()
  hash_dict.update(str.encode(value))
  return hash_dict.hexdigest()

# function to encrypt data
def encrypt_data(data, CONFIG):
  from cryptography.fernet import Fernet
  f = Fernet(CONFIG.ENCRYPTION_KEY.encode())

  token = f.encrypt(data)
  return token

# function to decrypt data
def decrypt_data(data, CONFIG):
  from cryptography.fernet import Fernet
  f = Fernet(CONFIG.ENCRYPTION_KEY.encode())

  token = f.decrypt(data)
  return token

# authenicate a person
def authenicate_person(user_name, password, config):
  try:
    # get person_id and salt from user_name data
    res = run_query(get_person_auth(user_name=user_name)).mappings().all()

    # can only return 1 valid row, if multiple or 0 rows are returned, cannot authenticate person
    if len(res) != 1:
      print('ERROR - Multiple or no users found')
      return 'Error'
    
    salt = res[0]['salt']
    password_hash = res[0]['password_hash']

    decrypted_salt = decrypt_data(salt, config)

    # hash inputted password
    hased_password = hash_value(password + decrypted_salt.decode()) + config.PEPPER

    if hased_password != password_hash:
      print('ERROR - Password does not match')
      return 'Error'
    
  except Exception as error:
    print('ERROR', error)
    return 'Error'

  return Person(person_id=res[0]['person_id'], user_name=res[0]['user_name'], first_name=res[0]['first_name'], last_name=res[0]['last_name'], email=res[0]['email']).as_dict()

# function to hash password and encrypt salt
def detrive_password_data(password, config_class):
  salt = generate_salt()                                                                # paerson salt
  encrypted_salt = encrypt_data(salt, config_class).decode()                            # encrypt salt
  password_hash = hash_value(password + salt.decode()) + config_class.PEPPER    # hash password

  return (password_hash, encrypted_salt)