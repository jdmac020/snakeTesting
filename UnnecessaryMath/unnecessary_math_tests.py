import unittest
import unnecessary_math as testClass

class TestUnnecessaryMath(unittest.TestCase):

	def setUp(self):
		pass
		
	def test_multiplyThreeAndFour_expectTweleve(self):
		self.assertEqual( testClass.multiply(3,4), 12)
		
	def test_multiplyThreeAndFive_expectFifteen(self):
		self.assertEqual( testClass.multiply(3,5), 12)
		
# actually runs the tests and provides the output
# run from command line with the -v flag for verbose output--why a test failed, what line, etc
if __name__ == '__main__':
	unittest.main()