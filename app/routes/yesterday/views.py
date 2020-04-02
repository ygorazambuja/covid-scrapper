import requests
from bs4 import BeautifulSoup

from . import yesterday_blueprint
from ...utils import fill_country_object


@yesterday_blueprint.route('/yesterday')
def get_yesterday_data():
    response = requests.get(
        'https://www.worldometers.info/coronavirus/').content
    soup = BeautifulSoup(response, 'html.parser')
    tbody = soup.find(id='main_table_countries_yesterday').find('tbody')
    rows = tbody.find_all('tr')
    countries = fill_country_object(rows)
    totalRow = soup.find_all(class_='total_row')[1]
    tds = totalRow.find_all('td')

    totalCases = tds[1].text
    newCases = tds[2].text
    totalDeaths = tds[3].text
    newDeaths = tds[4].text
    totalRecovered = tds[5].text
    activeCases = tds[6].text
    seriousCritical = tds[7].text
    totalCasesByMillionPop = tds[8].text
    totalDeathsByMillionPop = tds[9].text

    yesterdayData = {
        'total': {
            'totalCases': totalCases,
            'totalDeaths': totalDeaths,
            'newDeaths': newDeaths,
            'newCases': newCases,
            'totalRecovered': totalRecovered,
            'activeCases': activeCases,
            'seriousCritical': seriousCritical,
            'totalCasesByMillionPop': totalCasesByMillionPop,
            'totalDeathsByMillionPop':  totalDeathsByMillionPop, 'countries': countries,
        }
    }
    return yesterdayData
