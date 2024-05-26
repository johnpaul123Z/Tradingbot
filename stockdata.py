import requests
import json
from config import *

def bardata(name, timeframe):
    url = "https://data.alpaca.markets/v2/stocks/bars"
    
    params = {
        'symbols': name,
        'timeframe': timeframe,
        'start': '2022-01-03T00:00:00Z',
        'end': '2022-01-04T00:00:00Z'
    }
    headers = {
        "accept": "application/json",
        "APCA-API-KEY-ID": API_KEY,
        "APCA-API-SECRET-KEY": API_SECRET
    }
     
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    print(data)
    
bardata('spy','1Day')