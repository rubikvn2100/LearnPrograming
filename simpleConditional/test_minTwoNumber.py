import unittest
from minTwoNumber import minTwoNumber

class TestMinTwoNumber(unittest.TestCase):
    def test_twoIntegerInput(self):
        self.assertEqual(minTwoNumber(5, -3), -3)

if __name__ == "__main__":
    unittest.main()