import unittest
from unittest.mock import Mock
from RedditCrawler import RedditCrawler

class TestReddit(unittest.TestCase):
    def setUp(self):
        #this code will run before every single test
        self.reddit = RedditCrawler()
        pass

   # def setUpClass(self):
        #this code will run once before every single test
   #     pass

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
        pass

    def test_crawl(self):

        pass

if __name__ == '__main__':
    unittest.main()