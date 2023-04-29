import requests

# Get API key from CoinMarketCap
API_KEY = 'your-api-key-here'
endpoint = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': API_KEY
}
params = {
  'symbol': 'BTC'
}
response = requests.get(endpoint, headers=headers, params=params)
data = response.json()

# Parse the data to get the Bitcoin price
btc_price = data['data']['BTC']['quote']['USD']['price']
print(f"Current Bitcoin price is {btc_price:.2f} USD")
