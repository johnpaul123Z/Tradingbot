import pip._vendor.requests as requests
from config import *

BASE_URL = 'https://paper-api.alpaca.markets/v2'
ACCOUNT_URL = '{}/account'.format(BASE_URL)

def CREATE_ORDER(symbol, qty, notional, side, type,
                 time_in_force, limit_price, stop_price,
                 trail_price, trail_percent, extended_hours,
                 client_order_id, order_class, take_profit,
                 stop_loss, position_intent):
    PAYLOAD = {
        'APCA-API-KEY-ID':API_KEY,
        'APCA-API-SECRET-KEY':API_SECRET,
        "side": side,
        "type": type,
        "time_in_force": time_in_force,
        "symbol": symbol,
        "qty": qty,
        "notional": notional,
        "limit_price": limit_price,
        "stop_price": stop_price,
        "trail_price": trail_price,
        "trail_percent": trail_percent,
        "extended_hours": extended_hours,
        "client_order_id": client_order_id,
        "order_class": order_class,
        "take_profit": take_profit,
        "stop_loss":  stop_loss,
        "position_intent": position_intent
    
    }
    HEADERS = {
        "accept": "application/json",
        "content-type": "application/json"
    }

    RESPONSE = requests.post(ACCOUNT_URL, json=PAYLOAD, headers=HEADERS)
    PARSED_DATA = RESPONSE.json()
    return PARSED_DATA