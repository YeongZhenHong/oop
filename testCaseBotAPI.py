"""!
@file testCaseBotAPI
@author Liani Aslam 2609807A
@brief The following is the test cases for BotAPI.py
"""
import mysql.connector
import unittest
from BotAPI import BotAPI

class testBotAPI(unittest.TestCase):
    """! The BotAPI test case class.
    @brief Defines a testBotAPI class to test API call for each function.
    """
    
    def setUp(self): 
        """! Setup function to run before each function test
        """
        #this code will run before every single test
        self.botapi = BotAPI()
        self.message = "error"
        print("setting up BotAPI...")

    def tearDown(self):
        """! Teardown function to run after each function test
        """
        #this code will run after every single test
        print("tearing down BotAPI...")   

    def test_tweets(self):
        self.botapi.openCnx()
        self.assertTrue(self.botapi.insertTweets("test1", "test2", "1", "1", "1", "test3"))
        self.botapi.closeCnx()
    
    def test_reddit(self):
        self.botapi.openCnx()
        self.assertTrue(self.botapi.insertReddit("test1", "1", "1", "1"))
        self.botapi.closeCnx()

    def test_instagram(self):
        self.botapi.openCnx()
        self.assertTrue(self.botapi.insertInstagram("test1", "test2"))
        self.botapi.closeCnx()

    def test_yahoo(self):
        self.botapi.openCnx()
        self.assertTrue(self.botapi.insertYahoo("test1", "test2", "1", "test3", "test4"))
        self.botapi.closeCnx()

    
if __name__ == '__main__':
    unittest.main()

