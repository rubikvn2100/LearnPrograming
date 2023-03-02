import unittest
from isStringEmpty import isStringEmpty

class TestIsStringEmpty(unittest.TestCase):
    def test_nonEmptyStringInput(self):
        self.assertEqual(isStringEmpty("Cat"), False)

    def test_emptyStringInput(self):
        self.assertEqual(isStringEmpty(""), True)

if __name__ == "__main__":
    unittest.main()