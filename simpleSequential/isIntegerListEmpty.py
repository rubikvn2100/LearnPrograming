# Create a function that takes a list of integers as an input.
# Return True if the list is empty, and False otherwise.
# Ex:
#   isIntegerListEmpty([])        # return True
#   isIntegerListEmpty([0, 1, 2]) # return False
from typing import List

def isIntegerListEmpty(lst: List[int]) -> bool:
    return lst == []