import json
import os

import requests
from bs4 import BeautifulSoup
from flask import Flask

app = Flask(__name__)


@app.route('/')
def main_route():
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
        'div', style='font-size:13px; color:#999; text-align:center')[0].text
    activeCases = soup.find_all(class_='number-table-main')[0].text
    activeCasesMildCondition = soup.find_all(class_='number-table')[0].text
    activeCasesSeriousCondition = soup.find_all(class_='number-table')[1].text

    tbody = soup.find('tbody')
    rows = tbody.find_all('tr')

    countries = fill_country_object(rows)

    return {'confirmedCases': confirmedCases, 'deathCases': deathCases, "recovereds": recovered,
            'closedCases': closedCases, 'countries': countries, 'lastUpdate': lastUpdate, 'activeCases': activeCases,
            'activeCasesMildCondition': activeCasesMildCondition,
            'activeCasesSeriousCondition': activeCasesSeriousCondition}


@app.route('/country/<country>')
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


@app.route('/countries')
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


@app.route('/age')
def get_death_rate_by_age():
    response = requests.get(
        'https://www.worldometers.info/coronavirus/coronavirus-age-sex-demographics/').content
    soup = BeautifulSoup(response, 'html.parser')

    ageDeathTable = soup.find_all('tbody')[0]
    rows = ageDeathTable.find_all('tr')
    age = []
    for row in rows:
        cols = row.find_all('td')
        cols = [x.text.strip() for x in cols]

        age.append({cols[0]: {
            'deathRateConfirmedCases': cols[1],
            'deathRageAllCases': cols[2]
        }})
    del age[0]
    return json.dumps(age)


@app.route('/sex')
def get_death_rate_by_sex():
    response = requests.get(
        'https://www.worldometers.info/coronavirus/coronavirus-age-sex-demographics/').content
    soup = BeautifulSoup(response, 'html.parser')

    sexRatioTable = soup.find_all('tbody')[1]
    rows = sexRatioTable.find_all('tr')

    sex = []

    for row in rows:
        cols = row.find_all('td')
        cols = [x.text.strip() for x in cols]

        sex.append({cols[0]: {
            'deathRateConfirmedCases': cols[1],
            'deathRateAllCases': cols[2]
        }})

    del sex[0]
    return json.dumps(sex)


@app.route('/comorbidities')
def get_death_rate_by_comorbidities():
    response = requests.get(
        'https://www.worldometers.info/coronavirus/coronavirus-age-sex-demographics/').content
    soup = BeautifulSoup(response, 'html.parser')

    comorbiditiesTable = soup.find_all('tbody')[2]

    rows = comorbiditiesTable.find_all('tr')

    comorbidities = []

    for row in rows:
        cols = row.find_all('td')
        cols = [x.text.strip() for x in cols]

        comorbidities.append({
            cols[0]: {
                'deathRateConfirmedCases': cols[1],
                'deathRateAllCases': cols[2]
            }
        })
    del comorbidities[0]

    return json.dumps(comorbidities)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
