import unittest
from hasSpaceAtBeginning import hasSpaceAtBeginning

class TestHasSpaceAtBeginning(unittest.TestCase):
    def test_emptyListInput(self):
        self.assertEqual(hasSpaceAtBeginning(""), False)

    def test_noSpaceAtBeginning(self):
        self.assertEqual(hasSpaceAtBeginning("Hello World!"), False)

    def test_hasSpaceAtBeginning(self):
        self.assertEqual(hasSpaceAtBeginning(" Hello World!"), True)

if __name__ == "__main__":
    unittest.main()