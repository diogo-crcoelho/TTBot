# Copyright 2022 Diogo Coelho
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#Standard library imports
import os

# Third party imports
from dotenv import load_dotenv
import requests
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
