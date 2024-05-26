import pip._vendor.requests as requests
from config import *

BASE_URL = 'https://paper-api.alpaca.markets/v2'
ACCOUNT_URL = '{}/account'.format(BASE_URL)


def TEST_APLACA_ROUTE():
        r = requests.get(ACCOUNT_URL, headers={'APCA-API-KEY-ID':API_KEY,'APCA-API-SECRET-KEY':API_SECRET})
        TESTDATA = r.json()
        
        
        return TESTDATA['cash']
TEST_APLACA_ROUTE()