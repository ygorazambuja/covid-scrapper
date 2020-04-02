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


@app.route('/yesterday')
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
            'totalDeathsByMillionPop': cols[9],
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
    age = deleteFirstRow(rows)

    age[0][0] = 'eightyMore'
    age[1][0] = 'seventyToSeventyNine'
    age[2][0] = 'sixtyToSixtyNine'
    age[3][0] = 'fiftyToFiftyNine'
    age[4][0] = 'fortyToFortyNine'
    age[5][0] = 'thirtyToThirtyNine'
    age[6][0] = 'twentyToTwentyNine'
    age[7][0] = 'tenToNineteen'
    age[8][0] = 'zeroToNine'

    ageObj = []
    for key in age:
        ageObj.append({key[0]: {
            'deathRateConfirmedCases': key[1],
            'deathRateAllCases': key[2]
        }})
    return json.dumps(ageObj)


def deleteFirstRow(rows):
    temporary = []
    for row in rows:
        cols = row.find_all('td')
        cols = [x.text.strip() for x in cols]
        temporary.append(cols)
    del temporary[0]
    return temporary


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


@app.route('/news')
def get_news():
    response = requests.get(
        'https://www.worldometers.info/coronavirus/').content
    soup = BeautifulSoup(response, 'html.parser')

    newsLi = soup.find_all(class_='news_post')
    infos = {}
    count = 0

    for line in newsLi:
        source = []
        hrefs = line.find_all('a')
        for href in hrefs:
            if not '/coronavirus/country' in href.get('href'):
                source.append(href.get('href'))
        infos.update({count: {'info': line.text.strip(
            ' ').strip('\n').replace('\u00a0', ' ').replace('[source]', ''),
            'source': source}})
        count += 1
    return infos


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
