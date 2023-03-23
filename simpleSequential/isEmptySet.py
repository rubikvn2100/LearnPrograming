# Create a function that take one set of integers as input.
# Return True if the set is empty, otherwise return False.
# Ex:
#   isEmptySet({})     # Return True
#   isEmptySet({2, 3}) # Return False
from typing import Set

def isEmptySet(intSet: Set[int]) -> bool:
    return len(intSet) == 0