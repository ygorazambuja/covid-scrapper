import requests
from bs4 import BeautifulSoup
from flask import Flask

app = Flask(__name__)


@app.route('/covid')
def covid(request):
    response = requests.get('https://www.worldometers.info/coronavirus/').content
    soup = BeautifulSoup(response, 'html.parser')

    confirmedCases = soup.find_all('div', class_='maincounter-number')[0].text.strip(' ').strip('\n')
    deathCases = soup.find_all('div', class_='maincounter-number')[1].text.strip(' ').strip('\n')
    recovered = soup.find_all('div', class_='maincounter-number')[2].text.strip(' ').strip('\n')
    closedCases = soup.find('div', class_='number-table-main').text

    tbody = soup.find('tbody')
    rows = tbody.find_all('tr')

    countrys = {}

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
        countrys[country['name']] = country

    return {'confirmedCases': confirmedCases, 'deathCases': deathCases, "recovereds": recovered,
            'closedCases': closedCases, 'countrys': countrys}

#
# if __name__ == '__main__':
#     app.run(host='127.0.0.1', port='5000', debug=True)
