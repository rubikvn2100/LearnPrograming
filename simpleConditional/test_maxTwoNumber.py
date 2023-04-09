import unittest
from maxTwoNumber import maxTwoNumber

class TestMaxTwoNumber(unittest.TestCase):
    def test_twoIntegerInput(self):
        self.assertEqual(maxTwoNumber(5, -3), 5)

if __name__ == "__main__":
    unittest.main()