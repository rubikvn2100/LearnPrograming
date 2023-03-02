import unittest
from integerNegate import integerNegate

class TestIntegerNegate(unittest.TestCase):
    def test_postiveNumberInput(self):
        self.assertEqual(integerNegate(5), -5)
 
    def test_negativeNumberInput(self):
        self.assertEqual(integerNegate(-3), 3)

    def test_zeroNumberInput(self):
        self.assertEqual(integerNegate(0), 0)

if __name__ == "__main__":
    unittest.main()
