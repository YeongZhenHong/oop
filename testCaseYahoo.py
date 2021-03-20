import unittest
from YahooCrawler import Yahoo

class TestYahoo(unittest.TestCase):
    def setUp(self):
        #this code will run before every single test
        self.yahoo = Yahoo()

   # def setUpClass(self):
        #this code will run once before every single test
        pass

    def tearDown(self):
        #this code will run after every single test
        pass

    #def tearDownClass(self):
        #this code will run once after every single test
    #    pass
    def test_set_Settings(self):
        self.yahoo.set_Settings("food")
        self.assertEqual(self.yahoo.get_searchString(), "food")
        self.assertNotEqual(self.yahoo.get_searchString(), "food2")
    
    def test_get_article(self):
        pass

if __name__ == '__main__':
    unittest.main()
    
