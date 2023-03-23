import unittest
from isPerfectSquare import isPerfectSquare

class TestIsPerfectSquare(unittest.TestCase):
    def test_perfectSquareIntegerInput(self):
        self.assertEqual(isPerfectSquare(16), True)

    def test_nonPerfectSquareIntegerInput(self):
        self.assertEqual(isPerfectSquare(15), False)

    def test_negativeIntegerInput(self):
        self.assertEqual(isPerfectSquare(-3), False)

    def test_numberZeroInput(self):
        self.assertEqual(isPerfectSquare(0), True)

if __name__ == "__main__":
    unittest.main()