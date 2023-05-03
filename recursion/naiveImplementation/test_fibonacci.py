import unittest
from fibonacci import fibonacci

class TestFibonacci(unittest.TestCase):
    def test_negativeNumberInput(self):
        self.assertEqual(fibonacci(-5), -1)

    def test_positiveNumberInput(self):
        self.assertEqual(fibonacci(10), 55)

if __name__ == "__main__":
    unittest.main()
