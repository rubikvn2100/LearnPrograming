import unittest
from sortThreeNumberAscending import sortThreeNumberAscending

class TestSortThreeNumberAscending(unittest.TestCase):
    def test_listOfThreeIntegerInput(self):
        self.assertEqual(sortThreeNumberAscending([9, 1, 3]), [1, 3, 9])

if __name__ == "__main__":
    unittest.main()
