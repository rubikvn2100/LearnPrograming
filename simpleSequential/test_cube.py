import unittest
from cube import cube

class TestCubeFunction(unittest.TestCase):
    def test_positiveInput(self):
        self.assertEqual(cube(2), 8)

    def test_negativeInput(self):
        self.assertEqual(cube(-3), -27)

    def test_specialOneInput(self):
        self.assertEqual(cube(1), 1)

if __name__ =="__main__":
    unittest.main()
