import requests
from bs4 import BeautifulSoup
from flask import Flask

from app.routes.country import country_blueprint
from app.routes.statistics import statistics_blueprint
from app.routes.yesterday import yesterday_blueprint
from app.routes.home import home_blueprint
from app.utils import fill_country_object

app = Flask(__name__)


app.register_blueprint(country_blueprint)
app.register_blueprint(yesterday_blueprint)
app.register_blueprint(statistics_blueprint)
app.register_blueprint(home_blueprint)
