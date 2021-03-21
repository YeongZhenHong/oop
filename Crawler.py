"""! 
@file Crawler.py
@author Kendrick Ang 2609737A
@brief This file contains the Crawler Abstract Based class
@version 1.0
@section DESCRIPTION
An abstract based class for all crawlers.
"""

from abc import ABC, abstractmethod

class Crawler(ABC):
    """! The Abstract Based Class for crawlers.
    @brief Defines the base class utilized by all crawlers.
    """
    def __init__(self):
        """! The Crawler based class initializer.
        """
        self._searchString = ""
        self._searchLimit = 0

    def get_searchString(self):
        """! Retrieves the searchString value.
        @return The searchString value
        """
        return self._searchString

    def set_searchString(self, searchString):
        """! Sets the searchString value.
        @param searchString The search string data we want to crawl.
        """
        self._searchString = searchString
    
    def set_searchLimit(self, limit):
        self._searchLimit = limit

    def set_searchLimit(self, limit):
        """! Sets the searchLimit value.
        @param searchLimit The amount of posts that can be crawl.
        """
        self._searchLimit = limit

    def get_searchLimit(self):
        """! Retrieves the searchLimit value.
        @return The searchLimit value.
        """
        return self._searchLimit

    def set_Settings(self, searchString, searchLimit):
        """! Set the searchLimit and searchLimit value.
        @param searchString The search string data we want to crawl.
        @param searchLimit The amount of posts that can be crawl.
        """
        self.set_searchString(searchString)
        self.set_searchLimit(searchLimit)

    @abstractmethod
    def crawl(self):  
        """! Abstract class method.
        """
        pass