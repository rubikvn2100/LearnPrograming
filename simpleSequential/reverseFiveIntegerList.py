# Create a function that takes a list of five integers as an input.
# Return a new list which is the reverse of the original list.
# Ex:
#   reverseFiveIntegerList([-2, -1, 0, 1, 2]) # return [2, 1, 0, -1, -2]
#   reverseFiveIntegerList([3, 5, 9, -2, -7]) # return [-7, -2, 9, 5, 3]
from typing import List

def reverseFiveIntegerList(lst: List[int]) -> List[int]:
    return [lst[4], lst[3], lst[2], lst[1], lst[0]]