import os

import requests
from bs4 import BeautifulSoup
from flask import Flask

app = Flask(__name__)


@app.route('/')
def main_route():
    response = requests.get('https://www.worldometers.info/coronavirus/').content
    soup = BeautifulSoup(response, 'html.parser')

    confirmedCases = soup.find_all('div', class_='maincounter-number')[0].text.strip(' ').strip('\n')
    deathCases = soup.find_all('div', class_='maincounter-number')[1].text.strip(' ').strip('\n')
    recovered = soup.find_all('div', class_='maincounter-number')[2].text.strip(' ').strip('\n')
    closedCases = soup.find('div', class_='number-table-main').text
    lastUpdate = soup.find_all('div', style='font-size:13px; color:#999; text-align:center')[0].text

    tbody = soup.find('tbody')
    rows = tbody.find_all('tr')

    countries = fill_country_object(rows)

    return {'confirmedCases': confirmedCases, 'deathCases': deathCases, "recovereds": recovered,
            'closedCases': closedCases, 'countries': countries, 'lastUpdate': lastUpdate}


@app.route('/country/<country>')
def get_info_by_country(country):
    countryName = country

    response = requests.get('https://www.worldometers.info/coronavirus/').content
    soup = BeautifulSoup(response, 'html.parser')
    lastUpdate = soup.find_all('div', style='font-size:13px; color:#999; text-align:center')[0].text

    tbody = soup.find('tbody')
    rows = tbody.find_all('tr')

    countries = fill_country_object(rows)

    if countryName in countries:
        return {'country': countries[countryName], 'lastUpdate': lastUpdate}
        pass
    else:
        return {'error': 'Country does not exists, checkout for /countries'}


@app.route('/countries')
def get_countries_list():
    response = requests.get('https://www.worldometers.info/coronavirus/').content
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


def fill_country_object(rows):
    countries = {}
    for row in rows:
        cols = row.find_all('td')
        cols = [x.text.strip() for x in cols]

        country = {
            'name': cols[0],
            'totalCases': cols[1],
            'newCases': cols[2],
            'totalDeaths': cols[3],
            'newDeaths': cols[4],
            'totalRecovered': cols[5],
            'activeCases': cols[6],
            'seriousCritical': cols[7],
            'totalCasesByMillionPop': cols[8],
            'totalDeathsByMillionPop': cols[9]
        }
        countries[country['name']] = country
    return countries


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
