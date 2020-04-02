import requests
from bs4 import BeautifulSoup

from . import country_blueprint
from ...utils import fill_country_object


@country_blueprint.route('/country/<country>')
def get_info_by_country(country):
    countryName = country

    response = requests.get(
        'https://www.worldometers.info/coronavirus/').content
    soup = BeautifulSoup(response, 'html.parser')
    lastUpdate = soup.find_all(
        'div', style='font-size:13px; color:#999; text-align:center')[0].text

    tbody = soup.find('tbody')
    rows = tbody.find_all('tr')

    countries = fill_country_object(rows)

    if countryName in countries:
        return {'country': countries[countryName], 'lastUpdate': lastUpdate}
    else:
        return {'error': 'Country does not exists, checkout for /countries'}


@country_blueprint.route('/countries')
def get_countries_list():
    response = requests.get(
        'https://www.worldometers.info/coronavirus/').content
    soup = BeautifulSoup(response, 'html.parser')

    countries = []

    tbody = soup.find('tbody')
    rows = tbody.find_all('tr')

    for row in rows:
        cols = row.find_all('td')
        cols = [x.text.strip() for x in cols]

        country = cols[0]
        countries.append(country)
    return {'countries ': countries}
