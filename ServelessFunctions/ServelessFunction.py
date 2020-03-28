import sys
import json
import http.client
import collections



def main(params):
    country_name = params["location"]

    conn = http.client.HTTPSConnection("API url")
    headers = {
        'x-api-host': "HOST",
        'x-api-key': "API KEY"
        }

    conn.request("GET", "/statistics?country="+country_name, headers=headers)

    res = conn.getresponse()
    data = res.read()
    covid_data = json.loads(data)


    covid_statistics =  {
        "Country/Region": covid_data['response'][0]['country'],
        "Confirmed":covid_data['response'][0]['cases']['total'],
        "New cases":covid_data['response'][0]['cases']['new'],
        "Recovered":covid_data['response'][0]['cases']['recovered'],
        "Deaths":covid_data['response'][0]['deaths']['total']
    }

    return {"message": covid_statistics}
