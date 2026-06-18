# function to generate user salt
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

