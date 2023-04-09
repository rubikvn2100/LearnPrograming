import unittest
from hasSpaceAtEnd import hasSpaceAtEnd

class TestHasSpaceAtEnd(unittest.TestCase):
    def test_emptyListInput(self):
        self.assertEqual(hasSpaceAtEnd(""), False)

    def test_noSpaceAtTheEnd(self):
        self.assertEqual(hasSpaceAtEnd("Hello World!"), False)

    def test_hasSpaceAtTheEnd(self):
        self.assertEqual(hasSpaceAtEnd(" Hello World! "), True)

if __name__ == "__main__":
    unittest.main()