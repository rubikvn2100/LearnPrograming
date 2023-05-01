import unittest
from isPrime import isPrime

class TestIsPrime(unittest.TestCase):
    def test_primeNumberInput(self):
        self.assertEqual(isPrime(9), False)

    def test_nonPrimeNumberInput(self):
        self.assertEqual(isPrime(13), True)

if __name__ == "__main__":
    unittest.main()
