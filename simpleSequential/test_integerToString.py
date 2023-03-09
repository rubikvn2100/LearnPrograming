import unittest
from integerToString import integerToString

class testIntegerToString(unittest.TestCase):
    def test_negativeNumberInput(self):
        self.assertEqual(integerToString(-5), "-5")

    def test_positiveNumberInput(self):
        self.assertEqual(integerToString(10), "10")

    def test_zeroNumberInput(self):
        self.assertEqual(integerToString(0), "0")

if __name__ == "__main__":
    unittest.main()
