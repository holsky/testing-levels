import unittest
import sys
sys.path.append('..')

#import app
from levels_app import fizzbuzz

class UnitTest(unittest.TestCase):
	
	def test_given_1_answers_1(self):
		self.assertEqual("1", fizzbuzz(1))


if __name__ == '__main__':
	unittest.main()
