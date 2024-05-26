import requests
import json
from config import *

def bardata(name, timeframe):
    url = "https://data.alpaca.markets/v2/stocks/bars"
    
    params = {
        'symbols': name,
        'timeframe': timeframe,
        'start': '2024-05-21T00:00:00Z',
        'end': '2024-05-24T00:00:00Z'
    }
    headers = {
        "accept": "application/json",
        "APCA-API-KEY-ID": API_KEY,
        "APCA-API-SECRET-KEY": API_SECRET
    }
     #{'c': 477.71, 'h': 477.85, 'l': 473.85, 'n': 535425, 'o': 476.3, 't': '2022-01-03T05:00:00Z', 'v': 74528525, 'vw': 476.552376}
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    b=data['bars']['SPY']
    v=0
    for i in b:
        fbar= b[v]
        close = fbar['c']#close price 
        open = fbar['o'] #open price 
        high = fbar['h']#high  price 
        low = fbar['l']#low price 
        return ( high,low ,close)
        v+=1
bardata("spy", "1Day")