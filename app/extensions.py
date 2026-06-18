from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

from config import Config

# DB invocation 
db = SQLAlchemy()

# Object Relational Mapper
orm = db.orm

# DB Engine
Engine = db.create_engine(
  Config.SQLALCHEMY_DATABASE_URI,
  pool_size=20,
  max_overflow=5
)

# JWT Manager
jwt = JWTManager()