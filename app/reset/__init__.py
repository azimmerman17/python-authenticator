from flask import Blueprint

bp = Blueprint('reset', __name__, url_prefix='/reset')

from app.reset import routes
