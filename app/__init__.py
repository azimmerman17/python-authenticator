from flask import Flask

from config import Config

def create_app(config_class=Config):
  app = Flask(__name__)

  # Set Config varibles
  app.config.from_object(config_class)

  # Initialize Flask extensions

  # Migrate Models  

  # Register Blueprints

  # Define routes
  @app.route('/')
  def home():
    return '<p>Hello World</p>'

  return app