import unittest
from isPassingScore import isPassingScore

class TestIsPassingScore(unittest.TestCase):
    def test_scoreAboveOneHundedInput(self):
        self.assertEqual(isPassingScore(101), -1)

    def test_scoreBelowZeroInput(self):
        self.assertEqual(isPassingScore(-2), -1)

    def test_scoreBelowSixtyInput(self):
        self.assertEqual(isPassingScore(59), False)

    def test_scoreAboveSixtyInput(self):
        self.assertEqual(isPassingScore(61), True)