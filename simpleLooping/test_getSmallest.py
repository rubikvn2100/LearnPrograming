import unittest
from getSmallest import getSmallest

class TestGetSmallest(unittest.TestCase):
    def test_listOfInteger(self):
        self.assertEqual(getSmallest([-3, -2, -5, -9, 5]), -9)

if __name__ == "__main__":
    unittest.main()
