import json
import websocket
from Indicators import *
import pandas as pd
from config import API_KEY, API_SECRET

# Use the correct WebSocket endpoint for stock data
socket = 'wss://stream.data.alpaca.markets/v2/iex'  # Or 'wss://stream.data.alpaca.markets/v2/iex' based on your subscription level

# Authentication message
auth_message = {
    "action": "auth",
    "key": API_KEY,
    "secret": API_SECRET
}

subscription = {
    "action": "subscribe",
    "bars": ["SPY"]
}
timetamp =[]
open =[]
high =[]
low =[]
close = []
def on_message(ws, message):
    data = json.loads(message)
   
    if isinstance(data, list):
        for item in data:
            if 'T' in item and item['T'] == 'b':  
                bar = item
                timetamp.append(bar['t'])
                open.append(bar['o'])
                high.append(bar['h'])
                low.append(bar['l'])
                close.append(bar['c']) 
                si=Supertrend()
                a=si.runsupertrend(3,5,high,low,close) 
                print("supertrend data: ",a)
                         
   
def on_error(ws, error):
    print("Error:", error)

def on_close(ws):
    print("Connection closed")

def on_open(ws):
    ws.send(json.dumps(auth_message))
    ws.send(json.dumps(subscription))

ws = websocket.WebSocketApp(socket,
                            on_open=on_open,
                            on_message=on_message,
                            on_error=on_error,
                            on_close=on_close)

ws.run_forever()
