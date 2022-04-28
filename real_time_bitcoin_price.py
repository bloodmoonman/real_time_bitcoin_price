from requests import Request, Session
import json
import pprint 

url =  'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'

parameters = {
    'slug': 'bitcoin',
    'convert': 'USD'
}
#This is basically telling coinmarketcap api that we want json format in response -- application/json
headers = {
    'Accepts': 'application/json', 
    'X-CMC_PRO_API_KEY': '7d94dcdb-016c-453f-8a76-82c0d7805973' 
    }

#add these headers to sessions
#every single request we make now will use these headers 

session = Session()
session.headers.update(headers)

response = session.get(url, params=parameters)
pprint.pprint(json.loads(response.text)['data']['1']['quote']['USD']['price'])

