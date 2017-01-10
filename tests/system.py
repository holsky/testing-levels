import unittest
from selenium import webdriver

class SystemTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    def test_answer_1(self):
        self.driver.get('http://localhost:5000/1')
        self.assertEqual(
            self.driver.find_element_by_id('answer').text,
            '1')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
	unittest.main()
