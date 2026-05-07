import requests
import pandas as pd
from sqlalchemy import create_engine

import os
from dotenv import load_dotenv

load_dotenv()
COINS = ["btc-bitcoin",
         "eth-ethereum", "sol-solana", "xrp-xrp"
         ]

for coin_id in COINS:
    url = f"https://api.coinpaprika.com/v1/tickers/{coin_id}?quotes=USD"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        # print(data)
        df = pd.DataFrame(data)
        # print(df.columns)
        df = pd.json_normalize(data)
        DB_USER = os.getenv('DB_USER')
        DB_PASSWORD = os.getenv('DB_PASSWORD')
        DB_HOST = os.getenv('DB_HOST')
        DB_PORT = os.getenv('DB_PORT')
        DB_NAME = os.getenv('DB_NAME')
        engine = create_engine(
            f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

        df = df[['id', 'name', 'symbol', 'quotes.USD.price',
                 'quotes.USD.volume_24h', 'quotes.USD.market_cap']]

        df.to_sql("crypto_market_data", con=engine,
                  if_exists="append", index=False)

        print(df.head())
        # print(f"Sucessfully Retrieved Marker data for coin {coin_id}")
        # for market in data:

        #     print(f"Exchange: {market['ex change_name']}, Price: {market['quotes']['USD']}")
        # print(response.text)
        print(f"Sucessfully Retrieved data  for coin {coin_id}")
    else:
        print(f"Failed to retrieve data")
