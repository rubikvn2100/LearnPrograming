import unittest
from listGreatestCommonDivisor import listGreatestCommonDivisor

class TestListGreatestCommonDivisor(unittest.TestCase):
    def test_listOfInteger(self):
        self.assertEqual(listGreatestCommonDivisor([-42, 402, -66, 354, 78, 426]), 6)

    def test_twoZeroNumber(self):
        self.assertEqual(listGreatestCommonDivisor([0, 0]), -1)

if __name__ == "__main__":
    unittest.main()
