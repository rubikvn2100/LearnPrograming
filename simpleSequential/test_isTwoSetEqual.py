import unittest
from isTwoSetEqual import isTwoSetEqual

class TestIsTwoSetEqual(unittest.TestCase):
    def test_equalIntegerSetInput(self):
        self.assertEqual(isTwoSetEqual({6, 9}, {9, 6}), True)

    def test_nonEqualIntegerSetInput(self):
        self.assertEqual(isTwoSetEqual({2, 3}, {4, 5, 2 , 3}), False)

if __name__ == "__main__":
    unittest.main()