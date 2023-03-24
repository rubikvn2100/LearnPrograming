# Create a function that takes a list of integers as an input and returns the length of the list.
# Ex:
#   getIntegerListLength([])              # return 0
#   getIntegerListLength([0, 1, 2])       # return 3
#   getIntegerListLength([4, 3, 2, 1, 0]) # return 5
from typing import List

def getIntegerListLength(lst: List[int]) -> int:
    return len(lst)