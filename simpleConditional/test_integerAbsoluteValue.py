import unittest
from integerAbsoluteValue import integerAbsoluteValue

class TestIntegerAbsoluteValue(unittest.TestCase):
    def test_negativeIntegerInput(self):
        self.assertEqual(integerAbsoluteValue(-5), 5)

    def test_positiveIntegerInput(self):
        self.assertEqual(integerAbsoluteValue(12), 12)

    def test_numberZeroInput(self):
        self.assertEqual(integerAbsoluteValue(0), 0)

if __name__ == "__main__":
    unittest.main()