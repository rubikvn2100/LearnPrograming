import unittest
from squareFiveIntegerList import squareFiveIntegerList

class TestSquareFiveIntegerList(unittest.TestCase):
    def test_fiveIntegerInput(self):
        self.assertEqual(squareFiveIntegerList([2, 4, -3, -5, 1]), [4, 16, 9, 25, 1])

if __name__ == "__main__":
    unittest.main()