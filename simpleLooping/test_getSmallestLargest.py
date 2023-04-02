import unittest
from getSmallestLargest import getSmallestLargest

class TestGetSmallestLargest(unittest.TestCase):
    def test_listOfInteger(self):
        self.assertEqual(getSmallestLargest([-9, 3, 2, -2, -3, 9]), (-9, 9))

if __name__ == "__main__":
    unittest.main()
