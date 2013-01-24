import unittest
import NeedTest

class LearnUnitTest(unittest.TestCase):
	"""docstring for LearnUnitTest"""
	val = [(1,2), (2,5)]

	def testFunc(self):
		for a, b in self.val:
			result = NeedTest.addself(a)
			self.assertEqual(b, result)

if __name__ == '__main__':
	unittest.main()
