import unittest
from isPositive import isPositive

class TestIsFunction(unittest.TestCase):
    def test_positiveInput(self):
        self.assertEqual(isPositive(1), True)

    def test_negativeInput(self):
        self.assertEqual(isPositive(-2), False)

    def test_specialZeroInput(self):
        self.assertEqual(isPositive(0), False)
        

if __name__ == "__main__":
    unittest.main()