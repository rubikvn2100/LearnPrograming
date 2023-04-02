import unittest
from getLargest import getLargest

class TestGetLargest(unittest.TestCase):
    def test_listOfInteger(self):
        self.assertEqual(getLargest([-3, -2, 5, 9]), 9)

if __name__ == "__main__":
    unittest.main()