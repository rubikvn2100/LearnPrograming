import unittest
from countUnorderedAdditionOfSum import countUnorderedAdditionOfSum

class TestCountUnorderedAdditionOfSum(unittest.TestCase):
    def test_positiverIntegerInput(self):
        self.assertEqual(countUnorderedAdditionOfSum(9), 256)

    def test_negativeIntegerInput(self):
        self.assertEqual(countUnorderedAdditionOfSum(-5), 0)

    def test_zeroNumberInput(self):
        self.assertEqual(countUnorderedAdditionOfSum(0), 1)

if __name__ == "__main__":
    unittest.main()