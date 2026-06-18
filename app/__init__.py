from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

from app.extensions import db
from app.models import person
from config import Config

def create_app(config_class=Config):
  app = Flask(__name__)

  # Set Config varibles
  app.config.from_object(config_class)

  # Initialize Flask extensions
  db.init_app(app)
  jwt = JWTManager(app)

  # Migrate Models  
  Migrate(app, person.db)

  # Register Blueprints
  from app.auth import bp as auth_bp
  app.register_blueprint(auth_bp)

  # Define routes
  @app.route('/')
  def home():
    return '<p>Hello Auth</p>'

  return app