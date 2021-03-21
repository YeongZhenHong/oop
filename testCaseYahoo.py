"""!
@file testCaseYahoo.py
@author Kendrick Ang 2609737A / Sim Wei Jun Austin 2609730S
@brief This file contains the Yahoo test case class.
@version 1.0
@section DESCRIPTION
Runs Yahoo Crawler test cases
"""

import unittest
from unittest.mock import Mock, patch
from YahooCrawler import Yahoo

class TestYahoo(unittest.TestCase):
    """! The Yahoo test case cclass.
    @brief Defines a test Yahoo class to test yahooCrawler functions.
    """
    def setUp(self):
        """! Setup function to initialise an instance of Yahoo class to start testing.
        """
        self.yahoo = Yahoo()
        print("Setting up Yahoo Crawler...")

    def tearDown(self):
        """! Indicates that the test is completed.
        """
        print("Tearing down Yahoo Crawler...")

    def test_set_Settings(self):
        """! Test case for set settings.
        @brief Checks if the respective variables are assigned accordingly when passing it into the function.
        """
        print("Testing set_Settings")
        self.yahoo.set_Settings("food", 5)
        print("set_Settings called!")
        self.assertEqual(self.yahoo.get_searchString(), "food")
        self.assertNotEqual(self.yahoo.get_searchString(), "food2")
        print("get_searchString valid!")
        self.assertEqual(self.yahoo.get_searchLimit(), 5)
        self.assertNotEqual(self.yahoo.get_searchLimit(), 1)
        print("get_searchLimit valid!")
    
    @patch.object(Yahoo, 'get_article', return_value=None)
    def test_get_article(self, mock_method):
        """! Test case for get article function.
        @brief using patch.object to patch it as a mock method. 
        @brief Checks if get article function is called with the correct parameter.
        """
        self.yahoo.get_article("random")
        mock_method.assert_called_with("random")
        print("test_get_article valid!")

    @patch('builtins.open')
    def test_crawl(self,mock_open):
        """! Test case for crawl function.
        @brief Invalid the open module by patching it as a mock object
        as we do not want to export data to a file for the test.
        """
        #check if Exception is raised when passed in a negative/zero number or empty string
        with self.assertRaises(Exception) as context:
            self.yahoo.set_Settings("", 1)
            self.yahoo.crawl()

         #check if it indeed raise an exception error message when input a negative/zero number or an empty string
        self.assertTrue("Error, not a postive number or empty string" in str(context.exception))
        
        self.yahoo.set_Settings("foodpanda", 1)
        self.yahoo.crawl()
        print("Yahoo test_crawl valid!")

if __name__ == '__main__':
    unittest.main()
    
