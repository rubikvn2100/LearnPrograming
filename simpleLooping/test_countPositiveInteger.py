import unittest
from countPositiveInteger import countPositiveInteger

class testCountPositiveInteger(unittest.TestCase):
    def test_listOfIntegerInput(self):
        self.assertEqual(countPositiveInteger([-8, 2, 3, -1]), 2)

if __name__ == "__main__":
    unittest.main()
