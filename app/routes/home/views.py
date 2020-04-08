import requests
from bs4 import BeautifulSoup
from ...utils import fill_country_object

from . import home_blueprint


@home_blueprint.route('/')
def home():
    response = requests.get(
        'https://www.worldometers.info/coronavirus/').content
    soup = BeautifulSoup(response, 'html.parser')

    confirmedCases = soup.find_all(
        'div', class_='maincounter-number')[0].text.strip(' ').strip('\n')
    deathCases = soup.find_all(
        'div', class_='maincounter-number')[1].text.strip(' ').strip('\n')
    recovered = soup.find_all(
        'div', class_='maincounter-number')[2].text.strip(' ').strip('\n')
    closedCases = soup.find_all('div', class_='number-table-main')[1].text
    lastUpdate = soup.find_all(
        'div', style='font-size:13px; color:#999; margin-top:5px; text-align:center')[0].text
    activeCases = soup.find_all(class_='number-table-main')[0].text
    activeCasesMildCondition = soup.find_all(class_='number-table')[0].text
    activeCasesSeriousCondition = soup.find_all(class_='number-table')[1].text

    tbody = soup.find('tbody')
    rows = tbody.find_all('tr')

    countries = fill_country_object(rows)

    return {'confirmedCases': confirmedCases, 'deathCases': deathCases, "recovered": recovered,
            'closedCases': closedCases, 'countries': countries, 'lastUpdate': lastUpdate, 'activeCases': activeCases,
            'activeCasesMildCondition': activeCasesMildCondition,
            'activeCasesSeriousCondition': activeCasesSeriousCondition}
