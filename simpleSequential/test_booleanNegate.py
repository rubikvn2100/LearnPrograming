import unittest
from booleanNegate import booleanNegate

class TestBooleanNegateFunction(unittest.TestCase):
    def test_negateTrueInput(self):
        self.assertEqual(booleanNegate(True), False)

    def test_negateFalseInput(self):
        self.assertEqual(booleanNegate(False), True)

if __name__ == "__main__":
    unittest.main()
