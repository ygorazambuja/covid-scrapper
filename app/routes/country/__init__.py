from flask import Blueprint

country_blueprint = Blueprint('country_blueprint', __name__)

from . import views
