import os
import levels_app
import unittest
import sys
sys.path.append('..')

class IntegrationTest(unittest.TestCase):

# initialize levels_app for testing
    def setUp(self):
        levels_app.app.config['TESTING'] = True
        self.app = levels_app.app.test_client()

#test basic wiring
    def test_index(self):
        #returns Response object
        rv = self.app.get('/')
        #hint: rv.status
        self.assertTrue(False)
        

#test layers by calling for a number
    def test_fizzbuzz(self):
        #hint for comparison: b'1' in rv.data
        self.assertTrue(False)
        


if __name__ == '__main__':
    unittest.main()