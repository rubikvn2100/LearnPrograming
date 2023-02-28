import unittest
from countTrue5 import countTrue5

class TestCountTrue5Function(unittest.TestCase):
    def test_oneTrueInput(self):
        self.assertEqual(countTrue5(True, False, False, False, False), 1)
    
    def test_twoTrueInput(self):
        self.assertEqual(countTrue5(False, False, True, False, True), 2)

    def test_threeTrueInput(self):
        self.assertEqual(countTrue5(True, True, False, True, False), 3)
    
    def test_zeroTrueInput(self):
        self.assertEqual(countTrue5(False, False, False, False, False), 0)
    
    def test_allTrueInput(self):
        self.assertEqual(countTrue5(True, True, True, True, True), 5)

if __name__ == "__main__":
    unittest.main()
