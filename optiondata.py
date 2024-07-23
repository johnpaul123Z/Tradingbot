import requests
import pprint
from config import API_KEY, API_SECRET
# Define the base URL and endpoint for the API
base_url = "https://data.alpaca.markets/v1beta1/options/snapshots"

# Define your parameters
symbol = "AAPL"  # Replace with your desired symbol
feed = "indicative"  # or "nbbo" based on your subscription
limit = 100  # Adjust the limit as needed
updated_since = "2024-07-17"  # Replace with your start date

# Initialize parameters dictionary
params = {
    'feed': feed,
    'limit': limit,
    'updated_since': updated_since
}

headers = {
    "accept": "application/json",
    "APCA-API-KEY-ID": API_KEY,
    "APCA-API-SECRET-KEY": API_SECRET
}

def fetch_option_chain(base_url, symbol, params, headers):
    url = f"{base_url}/{symbol}"
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    return data

all_options = []

while True:
    data = fetch_option_chain(base_url, symbol, params, headers)
    
    if 'snapshot' in data:
        all_options.extend(data['snapshot']['options'])
    else:
        break  # No more option data, exit loop

    # Check if there is a next_page_token for pagination
    if 'next_page_token' in data:
        params['page_token'] = data['next_page_token']
    else:
        break  # No more pages, exit loop

pprint.pprint(all_options)