# Create a function that takes a list of integers as input.
# The function should return True if the list represents a binary value where it only contains values 0 or 1.
# Return False otherwise.
# Ex:
#   isBinaryList([0, 1, 2, 3, 4]) # return False
#   isBinaryList([1, 0, 0, 1, 1]) # return True
from typing import List

def isBinaryList(lst: List[int]) -> List[int]:
    for num in lst:
        if num != 0 and num != 1:
            return False

    return True
