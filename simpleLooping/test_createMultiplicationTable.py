import unittest
from createMultiplicationTable import createMultiplicationTable

class TestCreateMultiplicationTable(unittest.TestCase):
    def test_twoIntegerInput(self):
        self.assertEqual(createMultiplicationTable(2, 5), [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10]])

    def test_twoNumberZeroInput(self):
        self.assertEqual(createMultiplicationTable(0, 0), [])

if __name__ == "__main__":
    unittest.main()