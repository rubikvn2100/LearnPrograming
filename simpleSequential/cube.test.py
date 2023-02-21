import unittest
from cube import cube

class TestCubeFunction(unittest.TestCase):
    def test_cubeFuctionCase1(self):
        self.assertEqual(cube(2), 8, "Error: cube result is incorrect.")

    def test_cubeFuctionCase2(self):
        self.assertEqual(cube(-3), -27, "Error: cube result is incorrect.")

    def test_cubeFuctionCase3(self):
        self.assertEqual(cube(1), 1, "Error: cube result is incorrect.")

if __name__ =="__main__":
    unittest.main()   