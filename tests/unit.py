import unittest

#import app
from levels_app import fizzbuzz

class UnitTest(unittest.TestCase):
	
	def test_1_is_1(self):
		self.assertEqual("1", fizzbuzz(1))





if __name__ == '__main__':
	unittest.main()
