import unittest
from countPositiveAndNegativeInteger import countPositiveAndNegativeInteger

class TestCountPositiveAndNegativeInteger(unittest.TestCase):
    def test_listOfIntegerInput(self):
        self.assertEqual(countPositiveAndNegativeInteger([-9, -5, -2, -6, -3, 1]), (1, 5))

if __name__ == "__main__":
    unittest.main()
