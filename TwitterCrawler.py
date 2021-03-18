'''
Coded by Austin Sim Wei Jun 2609730S
'''

from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
import pandas as pd
import numpy as np
import json
from Crawler import Crawler

import Auth_Token 


class Twitter(Crawler):
    """! Analyze class
    Defining a tweet analyzer object to capture keyword input for the crawling of tweets.
    Outputs a csv file for processing in database.
    Contains initializer, authentication, crawling function and data processing.
    """

    def __init__(self):
        super().__init__()
        self.TweetList = []
    
    """! authenticate() function
    @brief returns API authentication for Twitter API, from the Auth_Token file.
    """

    def authenticate(self):
        auth = OAuthHandler(Auth_Token.CONSUMER_KEY,
                            Auth_Token.CONSUMER_SECRET)
        auth.set_access_token(Auth_Token.ACCESS_TOKEN,
                              Auth_Token.ACCESS_TOKEN_SECRET)
        api = API(auth)
        return api
    
    def set_Settings(self, searchString, limit):
        super().set_searchString(searchString)
        self.limit = limit
        
    """! tweets_to_df function.
    @param Tweets, an array of tweets to convert into a data frame format.
    @brief tweets_to_df(tweets) takes in a python list and converts it into a data frame,
    before returning a csv/json file
    """

    def tweets_to_df(self, tweets):
        # df = pd.DataFrame(data=[tweet.text for tweet in tweets])
        df = pd.DataFrame()
        df['content'] = np.array([tweet.text for tweet in tweets])
        df['author'] = np.array([tweet.user.screen_name for tweet in tweets])
        df['date'] = np.array([tweet.created_at for tweet in tweets])
        df['retweets'] = np.array([tweet.retweet_count for tweet in tweets])
        df['likes'] = np.array([tweet.favorite_count for tweet in tweets])
        df['url'] = np.array([tweet.id for tweet in tweets])
        # return df.to_json('tweets.json', orient='records', indent=1)
        return df.to_csv('tweets.csv')


    """! initTwitter function
    @brief takes calls authenticate() to allow the application
    to access twitter api,
    uses the Cursor function to search for a number of popular and recent tweets, based on
    the entered keyword.
    and calls tweets_to_df() function to generate a csv file.
    """

    def crawl(self):
        filter_list = self.get_searchString() + " -filter:retweets"
        api = self.authenticate()
        tweets = Cursor(api.search, q=filter_list, lang="en",
                        result_type="mixed").items(self.limit)
        tweetLi = []
        for tweet in tweets:
            tweetLi.append(tweet)
        df = self.tweets_to_df(tweetLi)


        # print(dir(tweetLi[0]))
        # print statement for output purposes, will delete after
