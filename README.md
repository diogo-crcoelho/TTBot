# TTBot

This projects utilizes Tweepy Wrapper and the CoinMarketCap API to tweet the price of DogeCoin

🔗  Key Links 🔗

https://docs.tweepy.org/en/stable/
https://coinmarketcap.com/api/documentation/v1/

# Installation and Running the script
1. Install dependencies
```
pip install -r reqs.txt
```
2. Follow from the [Google Cloud Platform](https://console.cloud.google.com/apis/credentials)

3. Save your Pushbullet token in a `.env` on the main directory. Example on the repository

4. To run simply
```
python run main.py
```

You can make it run periodically by assigning it to cronjob ou by using the APScheduler python module

# Disclaimer

Sometimes Google Calendar access token can expire. Can be solved by deletinng the `token.json` file and rerunning the script
