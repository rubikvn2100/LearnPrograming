import unittest
from normalizeString import normalizeString

class TestNormalizeString(unittest.TestCase):
    def test_ListStringWithSpaceInTheFront(self):
        self.assertEqual(normalizeString("  Hello World!"), "Hello World!")

    def test_listStringWithSpaceInTheEnd(self):
        self.assertEqual(normalizeString("Hello World!  "), "Hello World!")

    def test_listStringWithSpaceIntheMiddle(self):
        self.assertEqual(normalizeString("Hello  World!"), "Hello World!")

    def test_emptyStringInput(self):
        self.assertEqual(normalizeString(""), "")

if __name__ == "__main__":
    unittest.main()