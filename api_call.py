from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json, pprint

url2 = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

parameters = {
#   'start':'1',
#   'limit':'5000',
    # "id": 1,
    "symbol": "BTC",
    # "slug": "bitcoin"
    # 'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '534ea77e-5364-43ab-8c16-6e30c74ca1b8',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url2, params=parameters)
  data = json.loads(response.text)
  pprint.pprint(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)
  
