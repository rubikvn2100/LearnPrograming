# Create a function that take two set of integers and return the union of them
# Ex:
#   unionTwoSet({2, 3}, {3, 2}) # Return a set that equal to {2, 3}
#   unionTwoSet({2, 3}, {4, 3}) # Return a set that equal to {2, 3, 4}
#   unionTwoSet({2, 3}, {5, 4}) # Return a set that equal to {2, 3, 4, 5}
from typing import Set

def unionTwoSet(intSet1: Set[int], intSet2: Set[int]) -> Set[int]:
    return intSet1 | intSet2