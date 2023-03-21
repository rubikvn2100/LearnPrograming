import unittest
from listNextFiveNumber import listNextFiveNumber

class TestListNextFiveNumber(unittest.TestCase):
    def test_positiveIntegerInput(self):
        self.assertEqual(listNextFiveNumber(5), [6, 7, 8, 9, 10])

    def test_negativeIntegerInput(self):
        self.assertEqual(listNextFiveNumber(-9), [-8, -7, -6, -5, -4])

if __name__ == "__main__":
    unittest.main()
