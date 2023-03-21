import unittest
from listFourNeighborCoordinate import listFourNeighborCoordinate

class TestListFourNeighborCoordinate(unittest.TestCase):
    def test_tupleOfTwoIntegerInput(self):
        self.assertEqual(listFourNeighborCoordinate((5, 6)), [(5, 7), (5, 5), (6, 6), (4, 6)])

if __name__ == "__main__":
    unittest.main()