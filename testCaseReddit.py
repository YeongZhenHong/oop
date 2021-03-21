"""! 
@file testCaseReddit.py
@author Kendrick Ang 2609737A
@brief This file contains the Reddit test case class
@version 1.0
@section DESCRIPTION
Runs Reddit Crawler test cases
"""

import csv
import os
from logging import raiseExceptions
from unittest import mock
import praw
import unittest
from unittest.mock import Mock, patch
from RedditCrawler import RedditCrawler
from csv import reader

class TestReddit(unittest.TestCase):
    """! The test reddit class
    Defines a test reddit class to test redditCrawler functions
    """

    def setUp(self):
        """! Setup class to initialise an instance of RedditCrawler class to start testing
        """
        #this code will run before every single test
        self.reddit = RedditCrawler()
        self.message = "error"
        print("setting up Reddit Crawler...")

    def tearDown(self):
        """! Indicates that TestReddit is completed
        """
        #this code will run after every single test
        print("tearing down Reddit Crawler...")

    def test_setSettings(self):
        """! Test case for set settings.
        Checks if the respective variable is assigned accordingly when passed in the function.
        """
        self.reddit.setSettings("testCase", 6)
        self.assertEqual(self.reddit.get_searchString(), "testCase")
        self.assertEqual(self.reddit.get_searchLimit(), 6)
        self.assertNotEqual(self.reddit.get_searchString(), "food")
        self.assertNotEqual(self.reddit.get_searchLimit(), 9)
   
    def test_authenticate(self):
        """! Test case to check authentication
        Checks if the reddit creates an instance of praw.Reddit class.
        Also check if the passed in values for the praw.Reddit class are assigned accordingly.
        """
        #input Dummy data in the authenticate method
        self.reddit.authenticate("Dummy1", "Dummy2", "Dummy3")

        #checks whether the respective value are equal when passed-in
        self.assertEqual(self.reddit.reddit.config.client_id, "Dummy1")
        self.assertEqual(self.reddit.reddit.config.client_secret, "Dummy2")
        self.assertEqual(self.reddit.reddit.config.user_agent, "Dummy3")
        
        #check if reddit instance is called and created
        self.assertIsInstance(self.reddit.reddit, praw.Reddit, self.message)

    @patch.object(RedditCrawler, 'outputToFile', return_value=None)
    def test_crawl(self, mock_output):
        """! Test case for crawl function
        Invalid the outputToFile function by patching it as a mock object
        as we do not want to export data to a file
        """
        #check if ValueError is raised when passed in a negative/zero number
        with self.assertRaises(Exception) as context:
            self.reddit.setSettings("test", -1)
            self.reddit.crawl()
             #compares if the subreddit instance is called and created
            self.assertIsInstance(self.reddit.subreddit1, type(self.reddit.reddit.subreddit("singapore")), self.message)
        
        #check if it indeed raise an exception error message when input a negative/zero number
        self.assertTrue("Error, that is not a positive number!" in str(context.exception))

    def test_outputToFile(self):
        """! Test case to check output of data to .csv file.
        Compares the dummy data to the .csv file 
        """
        #create fake dummy data
        self.reddit.posts = [("test1", "test2","test3","test4")]
        self.reddit.outputToFile("test")
        testArr = ["test1", "test2","test3","test4"]

        try:
            #create a dummy file and make comparisons with the dummy data
            with open('_test.csv', 'r') as r:
                csv_reader = csv.reader(r)
                for row in csv_reader:
                    if row == ['Comment', 'Upvotes', 'Date', 'Time']:
                        self.assertEqual(row, ['Comment', 'Upvotes', 'Date', 'Time'] )
                    elif row == testArr:
                        self.assertEqual(row, testArr)
                    else:
                        raise Exception("Files are not equal!")
        except FileNotFoundError as error:
            print(error)
        finally:
            r.close()
            os.remove("_test.csv")

if __name__ == '__main__':
    unittest.main()