from dotenv import load_dotenv
import requests
import os
import json

load_dotenv()

def getPrice():
  """[Devolve detalhes do preço de dogecoin em euros]

  Returns:
      [json]: [Devolve detalhes do preço de dogecoin]
  """
  url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
  parameters = {
        'symbol':'DOGE',
        'convert': 'EUR'
  }
  headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': os.getenv("COIN_KEY"),
  }

  session = requests.Session()
  session.headers.update(headers)

  res = session.get(url, params=parameters)
  return json.loads(res.text)["data"]["DOGE"]["quote"]['EUR'] #returns the price of doge in eur