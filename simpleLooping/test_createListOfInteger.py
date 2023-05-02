import unittest
from createListOfInteger import createListOfInteger

class TestCreateListOfInteger(unittest.TestCase):
    def test_positiveIntegerInput(self):
        self.assertEqual(createListOfInteger(5), [0, 1, 2, 3, 4])

    def test_negativeIntegerInput(self):
        self.assertEqual(createListOfInteger(-2), [])

    def test_zeroNumberInput(self):
        self.assertEqual(createListOfInteger(0), [])

if __name__ == "__main__":
    unittest.main()