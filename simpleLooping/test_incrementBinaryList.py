import unittest
from incrementBinaryList import incrementBinaryList

class TestIncrementBinaryList(unittest.TestCase):
    def test_binaryIncrementOverflowBoundaryInput(self):
        self.assertEqual(incrementBinaryList([1, 1, 1, 1]), ([0, 0, 0, 0, 1]))

    def test_BinaryIncrementNonOverFlowInput(self):
        self.assertEqual(incrementBinaryList([1, 0, 0, 1]), ([0, 1, 0,1]))

    def test_nonBinaryListInput(self):
        self.assertEqual(incrementBinaryList([2, 3, 5, 9]), -1)

    def test_emptyListInput(self):
        self.assertEqual(incrementBinaryList([]), -1)

if __name__ == "__main__":
    unittest.main()