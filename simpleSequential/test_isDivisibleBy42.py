import unittest
from isDivisibleBy42 import isDivisibleBy42

class TestIsDivisibleBy42(unittest.TestCase):
    def test_isDivisibleBy42Input(self):
        self.assertEqual(isDivisibleBy42(84), True)
    
    def test_isNotDivisibleBy42Input(self):
        self.assertEqual(isDivisibleBy42(10), False)

if __name__ == "__main__":
    unittest.main()