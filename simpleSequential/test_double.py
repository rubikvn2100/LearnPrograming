import unittest
from double import double

class TestDoubleFunction(unittest.TestCase):
    def test_positiveInput(self):
        self.assertEqual(double(5), 10)

    def test_negativeInput(self):
        self.assertEqual(double(-3), -6)
    
    def test_specialZeroInput(self):
        self.assertEqual(double(0), 0)

if __name__ == "__main__":
    unittest.main()
