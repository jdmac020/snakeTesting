import unittest
import unnecessary_math as testClass

class TestUnnecessaryMath(unittest.TestCase):

	def setUp(self):
		pass
		
	def test_multiply3and4_return12(self):
		self.assertEqual( testClass.multiply(3,4), 12)
		
	def test_divide15by3_return5(self):
		self.assertEqual( testClass.divide(15,3), 5)
		
	def test_add12and12_return24(self):
		self.assertEqual( testClass.add(12,12), 24)
		
	def test_subtract5from12_return7(self):
		self.assertEqual( testClass.subtract(12,5), 7)
		
# actually runs the tests and provides the output
# run from command line with the -v flag for verbose output--why a test failed, what line, etc
if __name__ == '__main__':
	unittest.main()