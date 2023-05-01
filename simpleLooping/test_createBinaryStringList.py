import unittest
from createBinaryStringList import createBinaryStringList

class TestCreateBinaryStringList(unittest.TestCase):
    def test_simpleIntegerInput(self):
        self.assertEqual(createBinaryStringList(9), ['0', '1', '10', '11', '100', '101', '110', '111', '1000'])

if __name__ == "__main__":
    unittest.main()