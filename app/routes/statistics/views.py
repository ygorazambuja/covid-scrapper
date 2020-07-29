import json

import requests
from bs4 import BeautifulSoup

from . import statistics_blueprint
from ...utils import delete_first_row


@statistics_blueprint.route('/age')
def get_death_rate_by_age():
    response = requests.get(
        'https://www.worldometers.info/coronavirus/coronavirus-age-sex-demographics/').content
    soup = BeautifulSoup(response, 'html.parser')

    ageDeathTable = soup.find_all('tbody')[0]
    rows = ageDeathTable.find_all('tr')
    age = delete_first_row(rows)

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


@statistics_blueprint.route('/sex')
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


@statistics_blueprint.route('/comorbidities')
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


@statistics_blueprint.route('/news')
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
