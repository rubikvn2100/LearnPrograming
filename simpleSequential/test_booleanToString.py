import unittest
from booleanToString import booleanToString

class TestBooleanToString(unittest.TestCase):
    def test_trueBooleanInput(self):
        self.assertEqual(booleanToString(True), "True")

    def test_falseBooleanInput(self):
        self.assertEqual(booleanToString(False), "False")

if __name__ == "__main__":
    unittest.main()