import os
import tweepy as tw
import pandas as pd
from dotenv import load_dotenv
load_dotenv()


consumer_key= os.getenv("CONSUMER_KEY")
consumer_secret= os.getenv("CONSUMER_SECRET")
access_token= os.getenv("ACCESS_TOKEN")
access_token_secret= os.getenv("ACCESS_TOKEN_SECRET")

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

# Define the search term and the date_since date as variables
search_words = "#covid-19"
date_since = "2020-01-01"

# Collect tweets
tweets = tw.Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since).items(5)

# Iterate and print tweets
for tweet in tweets:
    print(tweet.text)
