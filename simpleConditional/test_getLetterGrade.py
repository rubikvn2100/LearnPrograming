import unittest
from getLetterGrade import getLetterGrade

class TestGetLetterGrade(unittest.TestCase):
    def test_scoreAboveOneHundedInput(self):
        self.assertEqual(getLetterGrade(101), -1)

    def test_scoreBelowZeroInput(self):
        self.assertEqual(getLetterGrade(-3), -1)

    def test_aboveNitetyGradeInput(self):
        self.assertEqual(getLetterGrade(91), 'A')

    def test_aboveEightyGradeInput(self):
        self.assertEqual(getLetterGrade(81), 'B')

    def test_aboveSeventyGradeInput(self):
        self.assertEqual(getLetterGrade(70), 'C')

    def test_aboveSixtyGradeInput(self):
        self.assertEqual(getLetterGrade(61), 'D')

    def test_belowSixtyGradeInput(self):
        self.assertEqual(getLetterGrade(20), 'F')

if __name__ == "__main__":
    unittest.main()
