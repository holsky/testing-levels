import os
import levels_app
import unittest
import sys
sys.path.append('..')

class IntegrationTest(unittest.TestCase):

    def setUp(self):
        levels_app.app.config['TESTING'] = True
        self.app = levels_app.app.test_client()

#test basic wiring
    def test_index(self):
        #returns Response object
        rv = self.app.get('/')
        self.assertEqual(rv.status, '200 OK')

#test the cut-through
    def test_fizzbuzz(self):
        rv = self.app.get('/1')
        self.assertEqual(rv.status, '200 OK')
        self.assertTrue(b'1' in rv.data)        


if __name__ == '__main__':
    unittest.main()