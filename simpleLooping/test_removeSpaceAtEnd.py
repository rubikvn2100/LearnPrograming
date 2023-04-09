import unittest
from removeSpaceAtEnd import removeSpaceAtEnd

class TestRemoveSpaceAtEnd(unittest.TestCase):
    def test_emptyList(self):
        self.assertEqual(removeSpaceAtEnd(""), "")

    def test_hasSpaceAtTheEndInput(self):
        self.assertEqual(removeSpaceAtEnd("Hello World!  "), "Hello World!")

    def test_noSpaceAtTheEndInput(self):
        self.assertEqual(removeSpaceAtEnd("Hello World!"), "Hello World!")

if __name__ == "__main__":
    unittest.main()
