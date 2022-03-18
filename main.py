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
import os, sys

# Third party imports
from dotenv import load_dotenv
import tweepy

# Local application imports# Local application imports
import coinmarket as cm

load_dotenv() #loads the env variables for the project from the .env file-- os.getenv to get the variable 

auth = tweepy.OAuthHandler(os.getenv("API_KEY"), os.getenv("API_SECRET"))
auth.set_access_token(os.getenv("ACESS_TOKEN"), os.getenv("AT_SECRET"))
API = tweepy.API(auth)

def tweet_price():
  """
  Tweets the price of Doge
  """
  data = cm.getPrice()
  price = "{:.6f}".format(data["price"])
  change24 = "{:.2f}".format(data["percent_change_24h"])
  change1 = "{:.2f}".format(data['percent_change_1h'])

  tweet = f"""$DOGE is {price}€ right now!!!
Thats {change1}% from last hour and a {change24}% difference in the last 24h"""
  API.update_status(tweet)

def main():
      tweet_price()

if __name__=="__main__":
  main()



    