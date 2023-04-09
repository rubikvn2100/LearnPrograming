import unittest
from minMaxTwoNumber import minMaxTwoNumber

class TestMinMaxTwoNumber(unittest.TestCase):
    def test_twoIntegerInput(self):
        self.assertEqual(minMaxTwoNumber(5, 4), (4, 5))

if __name__ == "__main__":
    unittest.main()