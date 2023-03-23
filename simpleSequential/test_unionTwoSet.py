import unittest
from unionTwoSet import unionTwoSet

class TestUnionTwoSet(unittest.TestCase):
    def test_equalIntegerSetInput(self):
        self.assertEqual(unionTwoSet({2, 3}, {3, 2}), {2, 3})

    def test_nonEqualIntegerSetInput(self):
        self.assertEqual(unionTwoSet({4, 5}, {6, 7}), {4, 5, 6, 7})

if __name__ == "__main__":
    unittest.main()