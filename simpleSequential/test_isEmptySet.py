import unittest
from isEmptySet import isEmptySet

class TestIsEmptySet(unittest.TestCase):
    def test_emptyIntegerSetInput(self):
        self.assertEqual(isEmptySet({}), True)

    def test_nonEmptyIntegerSetInput(self):
        self.assertEqual(isEmptySet({6, 9}), False)

if __name__ == "__main__":
    unittest.main()