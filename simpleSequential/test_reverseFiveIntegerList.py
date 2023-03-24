import unittest
from reverseFiveIntegerList import reverseFiveIntegerList

class TestReverseFiveIntegerList(unittest.TestCase):
    def test_fiveIntegerInput(self):
        self.assertEqual(reverseFiveIntegerList([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

if __name__ == "__main__":
    unittest.main()