import unittest
import sys
sys.path.append('..')

#import app
from levels_app import fizzbuzz

class UnitTest(unittest.TestCase):
	
	def test_given_1_answers_1(self):
		self.assertEqual("1", fizzbuzz(1))

	def test_given_2_answers_2(self):
		self.assertEqual("2", fizzbuzz(2))

	def test_given_3_answers_fizz(self):
		self.assertEqual("fizz", fizzbuzz(3))


if __name__ == '__main__':
	unittest.main()
