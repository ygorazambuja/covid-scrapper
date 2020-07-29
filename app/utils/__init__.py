def fill_country_object(rows):
    countries = {}
    for row in rows:
        cols = row.find_all('td')
        cols = [x.text.strip() for x in cols]

        country = {
            'name': cols[1],
            'totalCases': cols[2],
            'newCases': cols[3],
            'totalDeaths': cols[4],
            'newDeaths': cols[5],
            'totalRecovered': cols[6],
            'activeCases': cols[7],
            'seriousCritical': cols[8],
            'totalCasesByMillionPop': cols[9],
            'totalDeathsByMillionPop': cols[10],
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
