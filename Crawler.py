from abc import ABC, abstractmethod

class Crawler(ABC):
    """!
    The Abstract Based Class for crawlers 

    Defines the base class utilized by all crawlers.
    """
    def __init__(self):
        """! The Crawler based class initializer
        """
        self._searchString = ""

    def get_searchString(self):
        """! retrieves the search string value
        @return searchString value
        """
        return self._searchString

    def set_searchString(self, searchString):
        """! sets the searchString value
        @param searchString the search string data we want to crawl 
        """
        self._searchString = searchString

    @abstractmethod
    def crawl(self):  
        """! Abstract class method
        """
        pass