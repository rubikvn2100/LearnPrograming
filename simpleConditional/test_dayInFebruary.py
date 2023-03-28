import unittest
from dayInFebruary import dayInFebruary

class TestDayInFebruary(unittest.TestCase):
    def test_nonLeapYearInput(self):
        self.assertEqual(dayInFebruary(2023), 28)

    def test_leapYearInput(self):
        self.assertEqual(dayInFebruary(2024), 29)

if __name__ == "__main__":
    unittest.main()