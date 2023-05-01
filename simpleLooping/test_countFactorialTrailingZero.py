import unittest
from countFactorialTrailingZero import countFactorialTrailingZero

class TestCountFactorialTrailingZero(unittest.TestCase):
    def test_integerLessThanFive(self):
        self.assertEqual(countFactorialTrailingZero(4), 0)

    def test_integerLargerThanFive(self):
        self.assertEqual(countFactorialTrailingZero(11), 2)

if __name__ == "__main__":
    unittest.main()
