"""!
@file testCaseTwitter.py
@author Sim Wei Jun Austin 2609730S
@brief This file contains the Twitter test case class.
@version 1.0
@section DESCRIPTION
Running of Twitter Crawler test cases
"""


import unittest
from unittest.mock import Mock, patch
from TwitterCrawler import Twitter

class TestTwitter(unittest.TestCase):
        """! The Twitter test case class
        @brief Defining a TestTwitter class to test Twitter Crawler functions.
        """
        def setUp(self):
            self.twitter = Twitter()
            print("Setting up Twitter Crawler...")
        
        def tearDown(self):
            print("Tearing down Twitter Crawler...")
        
        def test_authenticate(self):
            self.twitter.authenticate()
             
        def test_set_Settings(self):
            print("Testing set_Settings")
            self.twitter.set_Settings("testCase", 10)
            print("set_Settings called!")
            self.assertEqual(self.twitter.get_searchString(),"testCase")
            self.assertNotEqual(self.twitter.get_searchString(),"nottestCase")
            print("get_searchString valid!")
            self.assertEqual(self.twitter.get_searchLimit(), 10)
            self.assertNotEqual(self.twitter.get_searchLimit(), 1)
            print("get_searchLimit valid!")
        
        @patch.object(Twitter, 'tweets_to_df', return_value=None)
        def test_tweets_to_df(self, mock_method):
            testLi = ['test','case']
            self.twitter.tweets_to_df(testLi)
            mock_method.assert_called_with(testLi)
            print("test_tweets_to_df valid!")

        @patch.object(Twitter, 'crawl', return_value=None)
        def test_crawl(self, mock_method):
            pass

if __name__ == "__main__":
    unittest.main() 