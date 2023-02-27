import unittest
from isNone import isNone

class TestIsNone(unittest.TestCase):
    def test_noneInput(self):
        self.assertEqual(isNone(None), True)
    
    def test_stringInput(self):
        self.assertEqual(isNone("Koffee"), False)

    def test_boolInput(self):
        self.assertEqual(isNone(False), False)
    
    def test_integerInput(self):
        self.assertEqual(isNone(2), False)
    
if __name__ == "__main__":
    unittest.main()
        