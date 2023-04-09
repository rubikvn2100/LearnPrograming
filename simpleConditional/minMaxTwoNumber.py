# Create a that takes two integers.
# Return a tuple of two integers representing the smallest and largest values in that order.
# Ex:
#   minTwoNumber(12, 3) # return (3, 12)
#   minTwoNumber(-2, 3) # return (-2, 3)
from typing import Tuple

def minMaxTwoNumber(n1: int, n2: int) -> Tuple[int, int]:
    return (n1, n2) if n1 < n2 else (n2, n1)
