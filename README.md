# TTBot

This projects utilizes Tweepy Wrapper and the CoinMarketCap API to tweet the price of DogeCoin

🔗  Key Links 🔗

https://docs.tweepy.org/en/v3.10.0/

https://coinmarketcap.com/api/documentation/v1/

# Installation and Running the script
1. Install dependencies
```
pip install -r reqs.txt
```
2. Follow instructions from [Tweepy authentication](https://docs.tweepy.org/en/v3.10.0/auth_tutorial.html) to generate Twitter API key and secret

3. Get CoinMarketCap API key as described in their [API Documentation](https://coinmarketcap.com/api/documentation/v1/)

3. Save your keyss and secret in a `.env` on the main directory.Follow the example  file on the repository

4. To run simply
```
python run main.py
```

You can make it run periodically by assigning it to cronjob ou by using the APScheduler python module


