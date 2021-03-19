"""! 
@file testCaseReddit.py
@author Kendrick Ang 2609737A
@brief This file contains the Reddit test class
@version 1.0
@section DESCRIPTION
Runs reddit testcase
"""

import praw
import unittest
from unittest.mock import Mock, patch
from RedditCrawler import RedditCrawler

class TestReddit(unittest.TestCase):
    def setUp(self):
        #this code will run before every single test
        self.reddit = RedditCrawler()
        self.DUMMYSETTINGS = {x:'dummy' for x in ['client_id', 'client_secret', 'user_agent']}

    #def setUpClass(self):
        #this code will run once before every single test
    #    pass

    def tearDown(self):
        #this code will run after every single test
        pass

    #def tearDownClass(self):
        #this code will run once after every single test
    #    pass

    def test_setSettings(self):
        self.reddit.setSettings("testCase", 6)
        self.assertEqual(self.reddit.get_searchString(), "testCase")
        self.assertEqual(self.reddit.limit, 6)
        self.assertNotEqual(self.reddit.get_searchString(), "food")
        self.assertNotEqual(self.reddit.limit, 9)

    def test_setLimit(self):
        self.reddit.setLimit(7)
        self.assertEqual(self.reddit.limit, 7)
        self.assertNotEqual(self.reddit.limit, 6)
   
    def test_authenticate(self):
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
        
        pass

    def test_outputToFile(self):
        
        pass
"""
  def test_example(self):
        mock_twitter = Mock()
        short_tweeter.tweet(mock_twitter, "message")
        mock_twitter.PostUpdate.assert_called_with("message")
"""
if __name__ == '__main__':
    unittest.main()