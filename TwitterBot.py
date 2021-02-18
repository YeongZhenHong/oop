from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API
from tweepy import Cursor
import pandas as pd
import numpy as np
import json

import twitter_credentials


def authenticate():
    auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
    auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
    api = API(auth)
    return api


class Analyze():
    def tweets_to_df(self, tweets):
        df = pd.DataFrame(data=[tweet.text for tweet in tweets])
        df['who'] = np.array([tweet.user.screen_name for tweet in tweets])
        df['date'] = np.array([tweet.created_at for tweet in tweets])
        df['retweets'] = np.array([tweet.retweet_count for tweet in tweets])
        df['likes'] = np.array([tweet.favorite_count for tweet in tweets])
        return df.to_json('tweets.json', orient='records', indent=1)


if __name__ == "__main__":
    tweet_analyzer = Analyze()
    keyword = "Austin OR Trump"
    filter_list = keyword + " -filter:retweets"
    api = authenticate()
    tweets = Cursor(api.search, q=filter_list, lang="en", result_type="popular").items(10)
    tweetLi = []
    for tweet in tweets:
        tweetLi.append(tweet)
    df = tweet_analyzer.tweets_to_df(tweetLi)
    print(dir(tweetLi[0]))




