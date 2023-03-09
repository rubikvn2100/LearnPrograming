import unittest
from floorDivision import floorDivision

class TestFloorDivision(unittest.TestCase):
    def test_twoPositiveNumberInput(self):
        self.assertEqual(floorDivision(10, 3), 3)

    def test_twoNegativeNumberInput(self):
        self.assertEqual(floorDivision(-7, -2), 3)

    def test_onePostiveAndOneNegativeInput(self):
        self.assertEqual(floorDivision(10, -2), -5)

    def test_divisibleNumberInput(self):
        self.assertEqual(floorDivision(10, 10), 1)

if __name__ == "__main__":
    unittest.main()