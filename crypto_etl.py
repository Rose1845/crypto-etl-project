import requests
# import pandas as pd

import os
# from load_dotenv import load_dotenv

# load_dotenv()
COINS = ["btc-bitcoin", "eth-ethereum", "sol-solana", "xrp-xrp"]


for coin_id in COINS:
    url = f"https://api.coinpaprika.com/v1/coins/{coin_id}"

    response = requests.get(url)

    if response.status_code == 200:
        print(f"Sucessfully Retrieved data for coin {coin_id}")
    else:
        print(f"Failed to retruve data")
