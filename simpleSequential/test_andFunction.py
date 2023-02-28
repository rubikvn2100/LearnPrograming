import unittest
from andFunction import andFunction

class TestAndFunction(unittest.TestCase):
    def test_diffBoolInput(self):
        self.assertEqual(andFunction(True, False), False)
    
    def test_sameBoolInput(self):
        self.assertEqual(andFunction(True, True), True)

if __name__ == "__main__":
    unittest.main()
