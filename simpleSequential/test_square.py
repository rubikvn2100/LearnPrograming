import unittest
from square import square

class TestSquareFunction(unittest.TestCase):
    def test_positiveInput(self):
        self.assertEqual(square(5), 25)

    def test_negativeInput(self):
        self.assertEqual(square(-3), 9)

    def test_specialZeroInput(self):
        self.assertEqual(square(0), 0)

if __name__ == "__main__":
    unittest.main()
