import unittest
from twoNumberGreatestCommonDivisor import twoNumberGreatestCommonDivisor

class TestTwoNumberGreatestCommonDivisor(unittest.TestCase):
    def test_twoPositiveIntegerInput(self):
        self.assertEqual(twoNumberGreatestCommonDivisor(24, 36), 12)

    def test_twoNegativeIntegerInput(self):
        self.assertEqual(twoNumberGreatestCommonDivisor(-6, -3), 3)

    def test_onePositiveAndOneNegativeIntegerInput(self):
        self.assertEqual(twoNumberGreatestCommonDivisor(-20, 48), 4)

    def test_twoZeroNumber(self):
        self.assertEqual(twoNumberGreatestCommonDivisor(0, 0), -1)

if __name__ == "__main__":
    unittest.main()