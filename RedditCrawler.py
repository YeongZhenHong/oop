"""! 
@file RedditCrawler.py
@author Kendrick Ang 2609737A / Sim Wei Jun Austin 2609730S
@brief This file contains the Reddit Crawler sub class
@version 1.0
@section DESCRIPTION
Runs reddit crawler to crawl data
@section usage_main Usage
e.g redditC = RedditCrawler()
    redditC.setSettings("foodpanda", 10)
    redditC.crawl()
"""

from logging import raiseExceptions
import praw
from prawcore import PrawcoreException
import csv
from Crawler import Crawler
from datetime import datetime
import Auth_Token

class RedditCrawler(Crawler):
    """! The reddit crawler sub class.
    @brief Defines a Reddit Crawler subclass to crawl reddit dataset.
    @brief Inherits from crawler based class.
    """
    def __init__(self):
        """! The reddit crawler class initializer.
        @param limit The amount of posts that can be crawled (optional)
        @return An instance of reddit crawler class initialized with specified limit and authenticates
        """
        #initialize super class
        super().__init__()

        #store a list of objects
        self.posts = []
        self.subreddit1 = None
        self.submission = None

        #authenticates and creates an instance of reddit so that we can start to scrape data 
        self.authenticate(Auth_Token.REDDIT_CLIENT,Auth_Token.REDDIT_SECRET, Auth_Token.REDDIT_AGENT)

    def authenticate(self, clientid, clientsecret, user):
        """! Authenticates the usage of scraping data from reddit and creates an instance of reddit.
        @param clientid     Input client_id from reddit
        @param clientsecret Input secret key from reddit
        @param user         Input user_agent(name) from reddit
        """
        #creates an instance of reddit with the specific information 
        self.reddit = praw.Reddit(client_id=clientid, client_secret=clientsecret, user_agent=user)
 
    def setSettings(self, searchString, searchLimit):
        """! Sets the search string and limit.
        @param searchString  The search string data we want to crawl 
        @param searchLimit   The amount of posts that can be crawled
        """
        #sets the searchString and searchLimit values in the super class
        super().set_Settings(searchString, searchLimit)
        
    def crawl(self):
        """! Main function to start crawling data and export it to .csv file.
        """
        #raise an exception if the searchLimit is not a positive number or the searchString is empty
        if super().get_searchLimit() < 0 or super().get_searchString() == "": 
            raise Exception("Error, not a postive number or empty string") 
        try:
            #navigates to subreddit "singapore", sets the search string and limits the posts
            self.subreddit1 = self.reddit.subreddit("singapore")
            self.submission = self.subreddit1.search(super().get_searchString(), limit=super().get_searchLimit())
           
            #in every submission, scrape the data we needed (comments, time, date)
            for post in self.submission:
                title = post.title
                url = post.permalink
                commentCount = post.num_comments
                upvotes = post.score
                
                post.comments.replace_more(limit=None)
                for comment in post.comments.list():
                    date = str(datetime.fromtimestamp(comment.created_utc))
                    datesplit = date.split(" ")
                    p = (comment.body, comment.author,datesplit[0], datesplit[1], comment.score)
                    #p = (title, comment.body, url, commentCount, datesplit[0], datesplit[1])
                    self.posts.append(p)
        except Exception as err:
           print(err)
        
        #output data to a .csv file
        self.outputToFile()

    def outputToFile(self,filename="_Reddit"):
        """! Export data to .csv file.
        @param filename Amend the export filename (optional)
        """
        try:
            with open('./CSV/'+super().get_searchString() + filename + '.csv', 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['Comment', 'Author', 'Date', 'Time', 'Upvotes'])
                #writer.writerow(['Title', 'Comment', 'Link', 'Comment Count', 'Date', 'Time'])
                writer.writerows(self.posts)
        except Exception as e:
            print(e)