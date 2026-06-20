import os
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()

import os
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()

class Config:
  TEST = os.environ.get('TEST')
  SQLALCHEMY_DATABASE_URI = os.environ.get('MYSQL_URI')
  PORT = os.environ.get('PORT')
  MYSQL_DATABASE = os.environ.get('MYSQL_DATABASE')
  MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD')
  MYSQL_PORT = os.environ.get('MYSQL_PORT')
  MYSQL_HOST = os.environ.get('MYSQL_HOST')
  MYSQL_URI = os.environ.get('MYSQL_URI')
  DEFAULT_SALT = os.environ.get('DEFAULT_SALT')
  ENCRYPTION_KEY = os.environ.get('ENCRYPTION_KEY')
  PEPPER = os.environ.get('PEPPER')
  ALGORITHM = os.environ.get('ALGORITHM')
  IV_LENGTH = os.environ.get('IV_LENGTH')
  JWT_SECRET = os.environ.get('JWT_SECRET')
  JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
  JWT_TOKEN_LOCATION = 'headers' 
  JWT_ALGORITHM= os.environ.get('JWT_ALGORITHM')
  JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=int(os.environ.get('JWT_ACCESS_TOKEN_EXPIRES')))

