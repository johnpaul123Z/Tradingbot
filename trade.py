import pip._vendor.requests as requests
from config import *

BASE_URL = 'https://paper-api.alpaca.markets/v2'
ACCOUNT_URL = '{}/account'.format(BASE_URL)

r = requests.get(ACCOUNT_URL, headers={'APCA-API-KEY-ID':API_KEY,'APCA-API-SECRET-KEY':API_SECRET})
print(r.content)