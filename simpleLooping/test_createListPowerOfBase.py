import unittest
from createListPowerOfBase import createListPowerOfBase

class TestCreateListPowerOfBase(unittest.TestCase):
    def test_twoIntegerInput(self):
        self.assertEqual(createListPowerOfBase(3, 3), [1, 3, 9])

    def test_powerIsZeroNumberInput(self):
        self.assertEqual(createListPowerOfBase(2, 0), [])

    def test_baseIsZeroNumberInput(self):
        self.assertEqual(createListPowerOfBase(0, 5), [0, 0, 0, 0, 0])

    def test_twoZeroNumberInput(self):
        self.assertEqual(createListPowerOfBase(0, 0), [])

if __name__ == "__main__":
    unittest.main()
