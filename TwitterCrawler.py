"""!
@file TwitterCrawler.py
@author Sim Wei Jun Austin 2609730S
@brief This file contains the TwitterCrawler class.
@version 1.0
@section DESCRIPTION
Runs the crawling function to get tweet content, likes and retweets.
"""
from tweepy import OAuthHandler, API, Cursor
import pandas as pd
import numpy as np
import json
from Crawler import Crawler

import Auth_Token


class Twitter(Crawler):
    """! Twitter class extends Crawler class.
    @brief Defining a tweet crawler object to crawl tweets.
    @brief Inputs include a search word and a search count.
    Contains initializer, authentication, crawling function and data processing.
    """

    def __init__(self):
        super().__init__()
        self.TweetList = []

    def authenticate(self):
        """! authenticate() function
        @brief returns API authentication for Twitter API, from the Auth_Token file.
        """
        auth = OAuthHandler(Auth_Token.CONSUMER_KEY,
                            Auth_Token.CONSUMER_SECRET)
        auth.set_access_token(Auth_Token.ACCESS_TOKEN,
                              Auth_Token.ACCESS_TOKEN_SECRET)
        api = API(auth)
        return api

    def set_Settings(self, searchString, limit):
        """! set_Settings() function
        @brief Sets a keyword to search for and the number of tweets to search for
        """
        super().set_searchString(searchString)
        self.limit = limit

    def tweets_to_df(self, tweets):
        """! tweets_to_df function.
        @param Tweets, an array of tweets to convert into a data frame format.
        @brief tweets_to_df(tweets) takes in a python list and converts it into a data frame,
        before returning a csv/json file
        """
        # df = pd.DataFrame(data=[tweet.text for tweet in tweets])
        df = pd.DataFrame()
        df['content'] = np.array([tweet.text for tweet in tweets])
        df['author'] = np.array([tweet.user.screen_name for tweet in tweets])
        df['date'] = np.array([tweet.created_at for tweet in tweets])
        df['retweets'] = np.array([tweet.retweet_count for tweet in tweets])
        df['likes'] = np.array([tweet.favorite_count for tweet in tweets])
        df['url'] = np.array([tweet.id for tweet in tweets])
        # return df.to_json('tweets.json', orient='records', indent=1)
        return df.to_csv('grabfood_tweets.csv')

    def crawl(self):
        """! crawl function inherited from Crawler class.
        @brief takes calls authenticate() to allow the application
        to access twitter api,
        uses the Cursor function to search for a number of popular and recent tweets, based on
        the entered keyword.
        and calls tweets_to_df() function to generate a csv file.
        """
        try:
            filter_list = self.get_searchString() + " -filter:retweets"
            api = self.authenticate()
            tweets = Cursor(api.search, q=filter_list, lang="en",
                            result_type="mixed").items(self.limit)
            tweetLi = []
            for tweet in tweets:
                tweetLi.append(tweet)
            df = self.tweets_to_df(tweetLi)
            return True
        except:
            print("cannot crawl")
            return False

# a = Twitter()
# a.set_Settings("grabfood", 35)
# a.crawl()
