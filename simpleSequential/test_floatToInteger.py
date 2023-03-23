import unittest
from floatToInteger import floatToInteger

class TestFloatToInteger(unittest.TestCase):
    def test_convertFloatToInteger(self):
        self.assertEqual(floatToInteger(2.14), 2)

if __name__ == "__main__":
    unittest.main()
