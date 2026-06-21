import secrets
from app.auth.functions import hash_value
  
# generates a 6 digit temporary token to reset the passsword
def generate_reset_token():
  # Generates a cryptographically secure 6-digit numeric string
  otp = ''.join(secrets.choice('0123456789') for _ in range(6))

  #hash for db
  hashted_otp = hash_value(otp)

  return otp, hashted_otp 