from flask import Blueprint

statistics_blueprint = Blueprint('statistics_blueprint', __name__)

from . import views
