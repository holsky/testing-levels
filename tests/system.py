import unittest
from selenium import webdriver
import sys
sys.path.append('..')

class SystemTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    def test_given_1_contains_answer_1(self):
        self.driver.get('http://localhost:5000/1')
        #hint for selection: self.driver.find_element_by_id('answer').text
        self.assertTrue(False)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
	unittest.main()
