import requests
from config import API_KEY, API_SECRET

def bardata(name, timeframe,starttime,endtime):
    url = "https://data.alpaca.markets/v2/stocks/bars"
    
    params = {
        'symbols': name,
        'timeframe': timeframe,
        'start': starttime,
        'end': endtime
    }
    headers = {
        "accept": "application/json",
        "APCA-API-KEY-ID": API_KEY,
        "APCA-API-SECRET-KEY": API_SECRET
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    bars = data['bars'][name]

    close = []
    open_prices = []
    high = []
    low = []
    
    for bar in bars:
        
        close.append(bar['c'])  # close price
        open_prices.append(bar['o'])  # open price
        high.append(bar['h'])  # high price
        low.append(bar['l'])  # low price
        
    return high, low, close
    
