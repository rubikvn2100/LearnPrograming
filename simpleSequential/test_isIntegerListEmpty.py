import unittest
from isIntegerListEmpty import isIntegerListEmpty

class TestIsIntegerListEmpty(unittest.TestCase):
    def test_emptyListInput(self):
        self.assertEqual(isIntegerListEmpty([]), True)

    def test_nonEmptyListInput(self):
        self.assertEqual(isIntegerListEmpty([1, 2, 3]), False)

if __name__ == "__main__":
    unittest.main()