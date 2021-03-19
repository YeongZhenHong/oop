import unittest
import cv2
from Sentimental_Analysis import Sentimental_Analysis


class Test_Sentimental_Analysis(unittest.TestCase):
    # indicate Sentimental Analysis Class is being tested
    @classmethod
    def setUpClass(cls):
        print('Setting up Sentimental Analysis Class\n')

    # indicate Sentimental Analysis Class finished testing
    @classmethod
    def tearDownClass(cls):
        print('\nClass test completed')

    def setUp(self):
        # Setup sequence where base cases are generated for comparison
        print('Setting up')
        self.everything = Sentimental_Analysis.clean(
            'test_clean_everything.csv')
        self.everything_result = 'file used testing clean function contains symbols like new lines numbers also contains links words also included end function return string characters lowercase'

        self.negative = Sentimental_Analysis.Analyse(
            'I really hated CSC1009 because I did not get to meet professor Harry. The professor that conducted the module is not as handsome as Harry')
        self.negative_result = (
            {'neg': 0.253, 'neu': 0.747, 'pos': 0.0, 'compound': -0.7976}, 'Negative Sentiment')

        self.positive = Sentimental_Analysis.Analyse(
            'I really enjoyed CSC1009 because professor Harry is conducting the module. Harry is a very handsome man')
        self.positive_result = (
            {'neg': 0.0, 'neu': 0.647, 'pos': 0.353, 'compound': 0.7956}, 'Positive Sentiment')
        self.neutral = Sentimental_Analysis.Analyse('')

        self.test_pos = {'neg': 0.0, 'neu': 0.647,
                         'pos': 0.353, 'compound': 0.7956}
        self.test_neg = {'neg': 0.253, 'neu': 0.747,
                         'pos': 0.0, 'compound': -0.7976}
        self.test_pos_img = cv2.imread('./test_pos.png')
        self.test_neg_img = cv2.imread('./test_neg.png')

    def tearDown(self):
        print('Test Completed\n')

    def test_clean(self):
        print('test_clean')
        # cleaned string == base cleanned string returns True
        self.assertEqual(self.everything, self.everything_result)
        # check if FileNotFoundError is raised when given a non-existenet file
        self.assertRaises(FileNotFoundError,
                          Sentimental_Analysis.clean, 'non-existent file.csv')

    def test_Analyse(self):
        print('test_analyse')
        # negative score == base negative score returns True
        self.assertEqual(self.negative, self.negative_result)
        #  postitive score == base postive score returns True
        self.assertEqual(self.positive, self.positive_result)

    def test_plotpie(self):
        print('test_plotpie')
        # Generate a positive image and compare against base test_pos_img
        Sentimental_Analysis.plot_pie(self.test_pos)
        # Check if images are the same size
        if self.test_pos_img.shape == cv2.imread('./sent_anal.png').shape:
            # subtract pixel count of images
            difference = cv2.subtract(
                self.test_pos_img, cv2.imread('./sent_anal.png'))
            # split pixel difference into blue red and green lists
            r, g, b = cv2.split(difference)
            # check if lists == 0, if the images are the same, r,b and g will be 0
            if cv2.countNonZero(r) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(b) == 0:
                self.assertTrue(True)
            # image not same force failure
            else:
                self.assertFalse(True)
        # image not same force failure
        else:
            self.assertFalse(True)

        # same procedure but this time generate a test_neg image and comapre with base test_neg_img
        Sentimental_Analysis.plot_pie(self.test_neg)
        if self.test_neg_img.shape == cv2.imread('./sent_anal.png').shape:
            difference = cv2.subtract(
                self.test_neg_img, cv2.imread('./sent_anal.png'))
            r, g, b = cv2.split(difference)
            if cv2.countNonZero(r) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(b) == 0:
                self.assertTrue(True)
            else:
                self.assertFalse(True)
        else:
            self.assertFalse(True)

        # same procedure but this time use previously generated test_neg image and compare against base test_pos_img
        # and return True if they are not the same
        if self.test_pos_img.shape == cv2.imread('./sent_anal.png').shape:
            difference = cv2.subtract(
                self.test_pos_img, cv2.imread('./sent_anal.png'))
            r, g, b = cv2.split(difference)
            if cv2.countNonZero(r) != 0 and cv2.countNonZero(g) != 0 and cv2.countNonZero(b) != 0:
                self.assertTrue(True)
            else:
                self.assertFalse(True)
        else:
            self.assertFalse(True)


if __name__ == '__main__':
    unittest.main()
