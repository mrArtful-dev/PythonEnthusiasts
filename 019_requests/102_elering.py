import requests
import datetime
import json

def get_electricity_prices():
    url = 'https://dashboard.elering.ee'
    endpoint = '/api/nps'
    start_date = datetime.datetime.now().isoformat(sep='T') + 'Z'
    end_date = (datetime.datetime.now() + datetime.timedelta(days=1)).isoformat(sep='T') + 'Z'
    req = requests.get(f'{url}{endpoint}/price?start={start_date}&end={end_date}')
    data = json.loads(req.content)
    return data

prices = get_electricity_prices()
for line in prices['data']['ee']:
    print(f'{datetime.datetime.fromtimestamp(line["timestamp"]).strftime("%d.%m %H:%M")}: {line["price"]}')

import pandas as pd

x = pd.DataFrame(prices['data']['ee'])
print(x['price'].mean())