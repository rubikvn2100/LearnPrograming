import unittest
from factorial import factorial

class TestFactorial(unittest.TestCase):
    def test_negativeNumberInput(self):
        self.assertEqual(factorial(-4), -1)

    def test_positiveNumberInput(self):
        self.assertEqual(factorial(5), 120)

    def test_zeroNumberInput(self):
        self.assertEqual(factorial(0), 1)

if __name__ == "__main__":
    unittest.main()
