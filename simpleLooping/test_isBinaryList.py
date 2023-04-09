import unittest
from isBinaryList import isBinaryList

class TestIsBinaryList(unittest.TestCase):
    def test_binaryListInput(self):
        self.assertEqual(isBinaryList([0, 1, 1, 0]), True)

    def test_nonBinaryListInput(self):
        self.assertEqual(isBinaryList([0, 1, 3, 4]), False)

if __name__ == "__main__":
    unittest.main()
