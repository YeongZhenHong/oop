"""! 
@file RedditCrawler.py
@author Kendrick Ang 2609737A
@brief This file contains the Reddit Crawler sub class
@version 1.0
@section DESCRIPTION
Runs reddit crawler to crawl data
@section usage_main Usage
e.g redditC = RedditCrawler()
    redditC.setSettings("foodpanda", 10)
    redditC.crawl()
"""

import praw
import csv
from Crawler import Crawler
from datetime import datetime
import Auth_Token

class RedditCrawler(Crawler):
    """! The reddit crawler sub class
    Defines a Reddit Crawler subclass to crawl reddit dataset.
    
    Inherits from crawler based class test
    """
    def __init__(self, limit=10):
        """! The reddit crawler class initializer
        @param limit The amount of posts that can be crawled (optional)
        @return An instance of reddit crawler class initialized with specified limit and authenticates
        """
        #initialize super class
        super().__init__()
        #store a list of objects
        self.posts = []
        self.limit = limit
        #authenticates and creates an instance of reddit so that we can start to scrape data 
        self.authenticate(Auth_Token.REDDIT_CLIENT,Auth_Token.REDDIT_SECRET, Auth_Token.REDDIT_AGENT)
    
    def authenticate(self, clientid, clientsecret, user):
        """! authenticates the usage of scraping data from reddit and creates an instance of reddit
        @param clientid     input client_id from reddit
        @param clientsecret input secret key from reddit
        @param user         input user_agent(name) from reddit
        """
        #creates an instance of reddit with the specific information 
        self.reddit = praw.Reddit(client_id=clientid, client_secret=clientsecret, user_agent=user)

    def setSettings(self, searchString, limit):
        """! sets the search string and limit
        @param searchString  the search string data we want to crawl 
        @param limit         the amount of posts that can be crawled
        """
        #sets the search string in the super class
        super().set_searchString(searchString)
        #limits the amount of post to be crawled
        self.setLimit(limit)

    def setLimit(self, limit):
        """! sets the limit to amount of posts that can be crawled
        @param limit the amount of posts that can be crawled
        """
        self.limit = limit

    def crawl(self):
        """! main function to start crawling data and export it to .csv file
        """
        #navigates to subreddit "singapore", sets the search string and limits the posts
        subreddit = self.reddit.subreddit("singapore")
        submission = subreddit.search(super().get_searchString(), limit=self.limit)

        #in every submission, scrape the data we needed (comments, time, date)
        for post in submission:
            title = post.title
            url = post.permalink
            commentCount = post.num_comments
            #upvotes = post.score
            
            try:
                for comment in post.comments.list():
                    date = str(datetime.fromtimestamp(comment.created_utc))
                    datesplit = date.split(" ")
                    #p = (comment.body, date)
                    p = (comment.body, comment.score, datesplit[0], datesplit[1])
                    # p = (title, comment.body, url, commentCount, datesplit[0], datesplit[1])
                    self.posts.append(p)
            except: 
                pass
        
        #output data to a .csv file
        self.outputToFile()

    def outputToFile(self,filename="reddit"):
        """! export data to .csv file
        @param filename amend the export filename (optional)
        """
        try:
            with open(super().get_searchString() + '_' + filename + '.csv', 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['Comment', 'Upvotes', 'Date', 'Time'])
                #writer.writerow(['Comment', 'Datetime',])
                #writer.writerow(['Title', 'Comment', 'Link', 'Comment Count', 'Date', 'Time'])
                writer.writerows(self.posts)
        except:
            print("Something went wrong")
