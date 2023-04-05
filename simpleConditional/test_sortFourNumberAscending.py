import unittest
from sortFourNumberAscending import sortFourNumberAscending

class TestSortFourNumberAscending(unittest.TestCase):
    def test_listOfFourIntegerInput(self):
        self.assertEqual(sortFourNumberAscending([5, 9, 3, 1]), [1, 3, 5, 9])

if __name__ == "__main__":
    unittest.main()
