import unittest
from removeSpaceAtBeginning import removeSpaceAtBeginning

class TestRemoveSpaceAtBeginning(unittest.TestCase):
    def test_emptyList(self):
        self.assertEqual(removeSpaceAtBeginning(""), "")

    def test_hasSpaceAtbeginingInput(self):
        self.assertEqual(removeSpaceAtBeginning("  Hello World!"), "Hello World!")

    def test_noSpaceAtBeginingInput(self):
        self.assertEqual(removeSpaceAtBeginning("Hello World! "), "Hello World! ")

if __name__ == "__main__":
    unittest.main()
