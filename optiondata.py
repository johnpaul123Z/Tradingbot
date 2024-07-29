import requests
from config import API_KEY, API_SECRET
def getochain(symbol):
    url = f"https://data.alpaca.markets/v1beta1/options/snapshots/{symbol}?feed=indicative&limit=2"
    headers = {
    "accept": "application/json",
    "APCA-API-KEY-ID":API_KEY ,
    "APCA-API-SECRET-KEY": API_SECRET
    }
    response = requests.get(url, headers=headers)
    data= response.json()
    return data

print(getochain('AAPL'))