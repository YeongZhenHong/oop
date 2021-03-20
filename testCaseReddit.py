"""! 
@file testCaseReddit.py
@author Kendrick Ang 2609737A
@brief This file contains the Reddit test case class
@version 1.0
@section DESCRIPTION
Runs Reddit Crawler testcase
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
        #self.DUMMYSETTINGS = {x:'dummy' for x in ['client_id', 'client_secret', 'user_agent']}
        print("setting up Reddit Crawler...")

    def tearDown(self):
        """! Indicates that the test is completed
        """
        #this code will run after every single test
        print("tearing down Reddit Crawler...")

    def test_setSettings(self):
        """! Test case for set settings.
        Checks if the respective variable is assigned accordingly when passed in the function.
        """
        self.reddit.setSettings("testCase", 6)
        self.assertEqual(self.reddit.get_searchString(), "testCase")
        self.assertEqual(self.reddit.limit, 6)
        self.assertNotEqual(self.reddit.get_searchString(), "food")
        self.assertNotEqual(self.reddit.limit, 9)

    def test_setLimit(self):
        """! Test case for set limit.
        Checks if the limit variable is assigned accordingly.
        """
        self.reddit.setLimit(7)
        self.assertEqual(self.reddit.limit, 7)
        self.assertNotEqual(self.reddit.limit, 6)
   
    def test_authenticate(self):
        """! Test case to check authentication
        Checks if the reddit creates an instance of praw.Reddit class.
        Also check if the passed in values for the praw.Reddit class are assigned accordingly.
        """
        self.reddit.authenticate("Dummy1", "Dummy2", "Dummy3")
        #self.reddit.reddit = Mock()
        #mock_test = Mock(spec=praw.Reddit)
        #print(mock_test.mock_calls)

        self.assertEqual(self.reddit.reddit.config.client_id, "Dummy1")
        self.assertEqual(self.reddit.reddit.config.client_secret, "Dummy2")
        self.assertEqual(self.reddit.reddit.config.user_agent, "Dummy3")
        
        #check if reddit instance is called and created
        message = "error"
        self.assertIsInstance(self.reddit.reddit, praw.Reddit, message)
        #self.reddit.reddit.assert_called_once_with({"d","d","d"})

    def test_crawl(self):
        """!
        """
        pass
    
    #@mock.patch('csv.writer'), csv_writer_mock in param
    def test_outputToFile(self):
        """! Test case to check output of data to .csv file.
        Compares the dummy data to the .csv file 
        """
        self.reddit.posts = [("test1", "test2","test3","test4")]
        self.reddit.outputToFile("test")

        testArr = ["test1", "test2","test3","test4"]

        try:
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
 
        #print(csv_writer_mock.mock_calls)
       # csv_writer_mock.assert_called_with([mock.call(['Comment', 'Upvotes', 'Date', 'Time'])])
       # self.assertEqual(csv_writer_mock.call_count, 1)
        #csv_writer_mock.writerow.assert_called_with([mock.call(['Comment', 'Upvotes', 'Date', 'Time'])])
        #csv_writer_mock.assert_any_call([mock.call(['Comment', 'Upvotes', 'Date', 'Time'])])
       # print(csv_writer_mock.writerow.assert_called_with())
        # csv_writer_mock.writerow.assert_has_calls('Comment', 'Upvotes', 'Date', 'Time')
    
"""
  def test_example(self):
        mock_twitter = Mock()
        short_tweeter.tweet(mock_twitter, "message")
        mock_twitter.PostUpdate.assert_called_with("message")
"""
if __name__ == '__main__':
    unittest.main()