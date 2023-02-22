import unittest
from double import double

class TestDoubleFunction(unittest.TestCase):
    def test_doubleFunctionCase1(self):
        self.assertEqual(double(5), 10, "Error: double result is incorrect.")

    def test_doubleFunctionCase2(self):
        self.assertEqual(double(-3), -6, "Error: double result is incorrect.")
    
    def test_doubleFunctionCase3(self):
        self.assertEqual(double(0), 0, "Error: double result is incorrect.")

if __name__ == "__main__":
    unittest.main()