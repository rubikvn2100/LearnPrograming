import unittest
from makeCoordinateTuple import makeCoordinateTuple

class TestMakeCoordinateTuple(unittest.TestCase):
    def test_twoIntegerSimplelInput(self):
        self.assertEqual(makeCoordinateTuple(2, 3), (2, 3))

if __name__ == "__main__":
    unittest.main()