import unittest
from isPositiveAndDivisibleBy69 import isPositiveAndDivisibleBy69

class TestsIsPositiveAndDivisibleBy69(unittest.TestCase):
    def test_positiveAndDivisibleBy69Input(self):
        self.assertEqual(isPositiveAndDivisibleBy69(69), True)

    def test_positiveAndNotDivisibleBy69Input(self):
        self.assertEqual(isPositiveAndDivisibleBy69(79), False)

    def test_negativeAndNotDivisibleBy69Input(self):
        self.assertEqual(isPositiveAndDivisibleBy69(-30), False)

    def test_negativeAndDivisibleby69Input(self):
        self.assertEqual(isPositiveAndDivisibleBy69(-69), False)

    def test_numberZeroInput(self):
        self.assertEqual(isPositiveAndDivisibleBy69(0), False)

if __name__ == "__main__":
    unittest.main()