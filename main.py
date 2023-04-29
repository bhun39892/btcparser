import requests
import argparse
import time

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

import requests
import argparse
import time

parser = argparse.ArgumentParser(description='Start Besu quickstart network')
parser.add_argument('--nodes', metavar='N', type=int, nargs='+', default=1,
                    help='number of nodes to start')
args = parser.parse_args()


def start():
    # Start network
    print("Starting Besu quickstart network...")
    subprocess.run(["docker-compose", "up", "--detach", "--scale", f"node={args.nodes}"])

    # Wait for network to start
    time.sleep(10)

    # Check Ethereum price
    response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd')
    eth_price = response.json()['ethereum']['usd']
    print(f"Current Ethereum price: {eth_price}")

try:
    start()
except KeyboardInterrupt:
    print("Shutdown requested. Exiting...")
    subprocess.run(["docker-compose", "down"])
