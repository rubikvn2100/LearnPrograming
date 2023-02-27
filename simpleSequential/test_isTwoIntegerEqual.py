import unittest
from isTwoIntegerEqual import isTwoIntegerEqual

class TestIsTwoIntegerEqual(unittest.TestCase):
    def test_equalIntegerInput(self):
        self.assertEqual(isTwoIntegerEqual(5, 5), True)
    
    def test_unEqualIntegerInput(self):
        self.assertEqual(isTwoIntegerEqual(3, 2), False)

if __name__ == "__main__":
    unittest.main()