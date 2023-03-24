import unittest
from getIntegerListLength import getIntegerListLength

class TestGetIntegerListLength(unittest.TestCase):
    def test_zeroIntegerListInput(self):
        self.assertEqual(getIntegerListLength([]), 0)

    def test_twoIntegerListInput(self):
        self.assertEqual(getIntegerListLength([1, 2]), 2)

if __name__ == "__main__":
    unittest.main()