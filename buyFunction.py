import requests
from config import API_KEY, API_SECRET

BASE_URL = 'https://paper-api.alpaca.markets/v2'
ORDERS_URL = '{}/orders'.format(BASE_URL)

def create_order(symbol, qty, side, order_type, time_in_force, option_symbol):
    payload = {
        'symbol': symbol,
        'qty': qty,
        'side': side,
        'type': order_type,
        'time_in_force': time_in_force,
        'option_symbol': option_symbol
    }
    headers = {
        'APCA-API-KEY-ID': API_KEY,
        'APCA-API-SECRET-KEY': API_SECRET,
        "accept": "application/json",
        "content-type": "application/json"
    }

    response = requests.post(ORDERS_URL, json=payload, headers=headers)
    parsed_data = response.json()
    return parsed_data


spy_call_option_symbol = "v"  
result = create_order(symbol='SPY', qty='1', side='buy', order_type='market', time_in_force='day', option_symbol=spy_call_option_symbol)
print(result)