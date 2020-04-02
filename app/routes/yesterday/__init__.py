from flask import Blueprint

yesterday_blueprint = Blueprint('yesterday_blueprint', __name__)

from . import views
