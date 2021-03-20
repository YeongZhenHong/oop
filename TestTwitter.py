import unittest
from unittest.mock import Mock
from TwitterCrawler import Twitter

class TestTwitter(unittest.TestCase):
        def setUp(self):
            self.twitter = Twitter()
            pass
        
        def test_setSettings(self):
            self.twitter.setSettings("testCase", 10)
            self.assertEqual(self.twitter.get_searchString(),"testCase")
            self.assertEqual(self.twitter.limit, 10)
            self.assertNotEqual(self.twitter.get_searchString(),"nottestCase")
            self.assertNotEqual(self.twitter.limit, 1)

        def test_authenticate(self):
            pass

        def test_crawl(self):
            pass

if __name__ == "__main__":
    unittest.main() 