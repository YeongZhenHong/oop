'''
Coded by Austin Sim Wei Jun 2609730S
'''
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API
from tweepy import Cursor
import pandas as pd
import numpy as np
import json

import auth_token


class Analyze():
    '''
    Analyze takes in user input as keyword, and generates tweets.json file
    '''
    def __init__(self,keyword):
        super().__init__()
        self.keyword=keyword
    '''
    @authenticate() takes in twitterAPI keys to grant the application access
    to twitter API
    '''

    def authenticate(self):
        auth = OAuthHandler(auth_token.CONSUMER_KEY,
                            auth_token.CONSUMER_SECRET)
        auth.set_access_token(auth_token.ACCESS_TOKEN,
                              auth_token.ACCESS_TOKEN_SECRET)
        api = API(auth)
        return api
    '''
    @tweets_to_df(tweets) takes in a python list and generates a json file  
    '''
    def tweets_to_df(self, tweets):
        df = pd.DataFrame(data=[tweet.text for tweet in tweets])
        df['who'] = np.array([tweet.user.screen_name for tweet in tweets])
        df['date'] = np.array([tweet.created_at for tweet in tweets])
        df['retweets'] = np.array([tweet.retweet_count for tweet in tweets])
        df['likes'] = np.array([tweet.favorite_count for tweet in tweets])
        # return df.to_json('tweets.json', orient='records', indent=1)
        return df.to_csv('tweets.csv')
    '''
    @initTwitter function takes calls authenticate() to allow the application
    to access twitter api 
    and calls tweets_to_df() function to generate a json file
    '''
    def initTwitter(self):
        filter_list = self.keyword + " -filter:retweets"
        api = self.authenticate()
        tweets = Cursor(api.search, q=filter_list, lang="en",
                        result_type="recent").items(100)
        tweetLi = []
        for tweet in tweets:
            tweetLi.append(tweet)
        df = self.tweets_to_df(tweetLi)
        # print(dir(tweetLi[0]))
        #print statement for output purposes, will delete after
getTweets = Analyze("foodpanda").initTwitter()