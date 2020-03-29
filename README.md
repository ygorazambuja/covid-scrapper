# covid-scrapper

## http://covid-web.herokuapp.com/

Application developed to monitor live covid data, and help with an abstraction for you to use in your frontend application.

#### https://www.worldometers.info/coronavirus/

The day is reset after midnight GMT+0

- Json Response &downarrow;

```jsonp
{
  "closedCases": "436,539",
  "confirmedCases": "597,267 ",
  "countrys": {
    //data for every country infected
  },
  "deathCases": "27,365",
  "recovereds": "133,363",
  "lastUpdate": "last updated info"
}
```

# endpoints

http://covid-web.herokuapp.com/ \
**/** \
brings all the info

http://covid-web.herokuapp.com/countries \
_/countries_ \
brings the list of the countries available

http://covid-web.herokuapp.com/country/Brazil \
**/countries/_countryAvailable_**

```json
{
  "country": {
    "activeCases": "3,378",
    "name": "Brazil",
    "newCases": "+60",
    "newDeaths": "+1",
    "seriousCritical": "296",
    "totalCases": "3,477",
    "totalCasesByMillionPop": "16",
    "totalDeaths": "93",
    "totalDeathsByMillionPop": "0.4",
    "totalRecovered": "6"
  },
  "lastUpdate": "Last updated: March 28, 2020, 05:22 GMT"
}
```

brings the info for the respective country

http://covid-web.herokuapp.com/comorbidities \
**/comorbidities**

```json
[
  {
    "Cardiovascular disease": {
      "deathRateConfirmedCases": "13.2%",
      "deathRateAllCases": "10.5%"
    }
  },
  {
    "Diabetes": {
      "deathRateConfirmedCases": "9.2%",
      "deathRateAllCases": "7.3%"
    }
  },
  {
    "Chronic respiratory disease": {
      "deathRateConfirmedCases": "8.0%",
      "deathRateAllCases": "6.3%"
    }
  },
  {
    "Hypertension": {
      "deathRateConfirmedCases": "8.4%",
      "deathRateAllCases": "6.0%"
    }
  },
  {
    "Cancer": {
      "deathRateConfirmedCases": "7.6%",
      "deathRateAllCases": "5.6%"
    }
  },
  {
    "no pre-existing conditions": {
      "deathRateConfirmedCases": "",
      "deathRateAllCases": "0.9%"
    }
  }
]
```

http://covid-web.herokuapp.com/age \
**/age**

```json
[
  {
    "eightyMore": {
      "deathRateConfirmedCases": "21.9%",
      "deathRateAllCases": "14.8%"
    }
  },
  {
    "seventyToSeventyNine": {
      "deathRateConfirmedCases": "",
      "deathRateAllCases": "8.0%"
    }
  },
  {
    "sixtyToSixtyNine": {
      "deathRateConfirmedCases": "",
      "deathRateAllCases": "3.6%"
    }
  },
  {
    "fiftyToFiftyNine": {
      "deathRateConfirmedCases": "",
      "deathRateAllCases": "1.3%"
    }
  },
  {
    "fortyToFortyNine": {
      "deathRateConfirmedCases": "",
      "deathRateAllCases": "0.4%"
    }
  },
  {
    "thirtyToThirtyNine": {
      "deathRateConfirmedCases": "",
      "deathRateAllCases": "0.2%"
    }
  },
  {
    "twentyToTwentyNine": {
      "deathRateConfirmedCases": "",
      "deathRateAllCases": "0.2%"
    }
  },
  {
    "tenToNineteen": {
      "deathRateConfirmedCases": "",
      "deathRateAllCases": "0.2%"
    }
  },
  {
    "zeroToNine": {
      "deathRateConfirmedCases": "",
      "deathRateAllCases": "no fatalities"
    }
  }
]
```

http://covid-web.herokuapp.com/sex \
**/sex**

```json
[
  {
    "Male": {
      "deathRateConfirmedCases": "4.7%",
      "deathRateAllCases": "2.8%"
    }
  },
  {
    "Female": {
      "deathRateConfirmedCases": "2.8%",
      "deathRateAllCases": "1.7%"
    }
  }
]
```

http://covid-web.herokuapp.com/yesterday \
**/yesterday**

```json
{
    {
    "total": {
        "activeCases": "490,746",
        "countries": {
        },
        "newDeaths": "+3,516",
        "seriousCritical": "25,351",
        "totalCases": "663,079",
        "totalCasesByMillionPop": "85.1",
        "totalDeaths": "30,857",
        "totalDeathsByMillionPop": "4.0",
        "totalRecovered": "141,476"
    }
}
```

as I add new features I will go up
