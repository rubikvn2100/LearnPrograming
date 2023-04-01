import unittest
from sumIntegerSquareToN import sumIntegerSquareToN

class TestSumIntegerSquareToN(unittest.TestCase):
    def test_negativeIntegerInput(self):
        self.assertEqual(sumIntegerSquareToN(-5), -1)

    def test_positiveIntegerInput(self):
        self.assertEqual(sumIntegerSquareToN(3), 5)

if __name__ == "__main__":
    unittest.main()
