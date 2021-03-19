"""!
@file TelegramTest.py
@author Yeong Zhen Hong 2609703Y
@brief The following is the test cases for TelegramBot.py
"""

import unittest
from TelegramBot import TelegramBot 


class TelegramTest(unittest.TestCase):
    """! TelegramTest class
    Test cases for TelegramBot.py
    Due to the need to wrap several functions with python-telegram-bot
    library, several functions of TelegramBot.py could not be written in a test case
    the following are the functions that can actually be written in a test case
    """
    initTeleBot = TelegramBot()
    
    def testSartBot(self):
        """! Test Start Bot Function
        @brief test if the bots can start successfully
        """
        self.assertTrue(self.initTeleBot.startBot())

    def testHandlers(self):
        """! Test handlers
        @brief Test if the handlers can be injected to allow the bot to take in user commands
        """
        self.assertTrue(self.initTeleBot.injectHandlers())
        
    def testkillBot(self):
        """! Test killing of bot process
        @brief Test if the bot process can be killed successfully
        """
        self.assertTrue(self.initTeleBot.killBot())

    

if __name__ == '__main__': 
    unittest.main()