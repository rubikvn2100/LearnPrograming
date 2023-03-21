import unittest
from addTwoNumericalString import addTwoNumericalString

class TestAddTwoNumericalString(unittest.TestCase):
    def test_twoPositiveNumberInput(self):
        self.assertEqual(addTwoNumericalString("5", "5"), "10")

    def test_twoNegativeNumberInput(self):
        self.assertEqual(addTwoNumericalString("-3", "-3"), "-6")

    def test_onePositiveOneNegativeInput(self):
        self.assertEqual(addTwoNumericalString("-5", "3"), "-2")

    def test_oneZeroOnePositiveInput(self):
        self.assertEqual(addTwoNumericalString("0", "3"), "3")

    def test_oneZeroOneNegativeInput(self):
        self.assertEqual(addTwoNumericalString("0", "-4"), "-4")

if __name__ == "__main__":
    unittest.main()
