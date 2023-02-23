import unittest
from orFunction import orFunction

class TestOrFunction(unittest.TestCase):
    def test_trueTrueInput(self):
        self.assertEqual(orFunction(True, True), True)

    def test_trueFalseInput(self):
        self.assertEqual(orFunction(True, False), True)

    def test_falseTrueInput(self):
        self.assertEqual(orFunction(False, True), True)

    def test_falseFalseInput(self):
        self.assertEqual(orFunction(False, False), False)
    
if __name__ == "__main__":
    unittest.main()
