import unittest
from sumIntegerToN import sumIntegerToN

class TestSumIntegerToN(unittest.TestCase):
    def test_negativeIntegerInput(self):
        self.assertEqual(sumIntegerToN(-5), -1)

    def test_postivieIntgegerInput(self):
        self.assertEqual(sumIntegerToN(3), 3)

if __name__ == "__main__":
    unittest.main()
