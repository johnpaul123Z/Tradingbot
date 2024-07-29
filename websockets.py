import json
import rel
import websocket
from Indicators import *
from config import*
dataset = 'us_stocks_essential'
tickers = ['TSLA']
open =[]
high =[]
low =[]
close = []
sth=[]
stl=[]
Stt=[]
Stt.append(0)
def on_message(wsapp, message):
     data = json.loads(message)
     if isinstance(data, dict):
        # Extract the bar data
        
        open.append(data['o'])
        high.append(data['h'])
        low .append(data['l'])
        close.append(data['c'])
        si=Supertrend() 
        b,a,St1=si.runsupertrend(3, 3,high,low,close,sth,stl,Stt)
        Stt.append(St1)
        if(a!=0):
            sth.append(a)
            stl.append(b)
        print("supertrend data: ",a,b," supertrend direction :", St1)
       
        
        
def on_error(wsapp, error):
    print(f'Error: {error}')


def on_close(wsapp, close_status_code, close_msg):
    print('Connection is closed')


def on_open(wsapp):
    print('Connection is opened')
    subscribe(wsapp, dataset, tickers)


def subscribe(wsapp, dataset, tickers):
    sub_request = {
        'event': 'subscribe',
        'dataset': dataset,
        'tickers': tickers,
        'channel': 'bars',
        'frequency': '1m',
        'aggregation': '1m'
    }
    wsapp.send(json.dumps(sub_request))
if __name__ == '__main__':
    # Open ws connection
    ws = websocket.WebSocketApp(f'wss://ws.finazon.io/v1?apikey={api_key}',
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error)
    # Start event loop
    ws.run_forever(
        # Set dispatcher to automatic reconnection, 5 second reconnect delay if connection closed unexpectedly
        dispatcher=rel, reconnect=5,
        # Sending ping with specified interval to prevent disconnecting
        ping_interval=30, ping_timeout=10,
    )
    # Handle Keyboard Interrupt event
    rel.signal(2, rel.abort)
    rel.dispatch()