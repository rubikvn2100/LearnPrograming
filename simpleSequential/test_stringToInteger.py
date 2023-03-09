import unittest
from stringToInteger import stringToInteger

class testStringToInteger(unittest.TestCase):
    def test_positiveNumericalStringInput(self):
        self.assertEqual(stringToInteger("5"), 5)

    def test_negativeNumericalStringInput(self):
        self.assertEqual(stringToInteger("-6"), -6)

    def test_zeroNumericalStringInput(self):
        self.assertEqual(stringToInteger("0"), 0)

if __name__ == "__main__":
    unittest.main()