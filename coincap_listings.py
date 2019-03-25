import json
import requests

listing_url = 'https://api.coinmarketcap.com/v2/listings/'

request = requests.get(listing_url)
results = request.json()

data = results['data']

for currency in data:
    rank = currency['id']
    name = currency['name']
    symbol = currency['symbol']
    print(str(rank) + ':' + name + '(' + symbol + ')')
