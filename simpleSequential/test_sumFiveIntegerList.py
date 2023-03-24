import unittest
from sumFiveIntegerList import sumFiveIntegerList

class TestSumFiveIntegerList(unittest.TestCase):
    def test_fiveIntegerInput(self):
        self.assertEqual(sumFiveIntegerList([1, 2, 0, -1, 5]), 7)

if __name__ == "__main__":
    unittest.main()