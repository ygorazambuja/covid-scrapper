# covid-scrapper



## http://covid-web.herokuapp.com/

Application developed to monitor live covid data, and help with an abstraction for you to use in your frontend application.

#### https://www.worldometers.info/coronavirus/

The day is reset after midnight GMT+0


* Json Response &downarrow;
````jsonp
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

````

#endpoints

**/** \
brings all the info

**/countries* \
brings the list of the countries available

**/countries/_countryAvailable_** \
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


as I add new features I will go up