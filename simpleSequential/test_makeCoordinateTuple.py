import unittest
from makeCoordinateTuple import makeCoordinateTuple

class TestMakeCoordinateTuple(unittest.TestCase):
    def test_twoPositiveNumericalInput(self):
        self.assertEqual(makeCoordinateTuple(2, 3), (2, 3))

    def test_twoNegativeNumericalInput(self):
        self.assertEqual(makeCoordinateTuple(-3, -4), (-3, -4))

    def test_onePositiveOneNegativeNumericalInput(self):
        self.assertEqual(makeCoordinateTuple(-5, 6), (-5, 6))

if __name__ == "__main__":
    unittest.main()