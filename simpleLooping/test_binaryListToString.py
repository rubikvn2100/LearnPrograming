import unittest
from binaryListToString import binaryListToString

class TestBinaryListToString(unittest.TestCase):
    def test_listBinaryInput(self):
        self.assertEqual(binaryListToString([0, 1, 1, 0, 0, 1]), "100110")

    def test_notListBinaryInput(self):
        self.assertEqual(binaryListToString([2, 4, 6]), -1)

    def test_emptyList(self):
        self.assertEqual(binaryListToString([]), -1)

if __name__ == "__main__":
    unittest.main()