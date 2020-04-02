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


def delete_first_row(rows):
    temporary = []
    for row in rows:
        cols = row.find_all('td')
        cols = [x.text.strip() for x in cols]
        temporary.append(cols)
    del temporary[0]
    return temporary
