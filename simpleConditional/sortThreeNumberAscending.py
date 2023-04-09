# Create a function that takes a list of three integers as input.
# Return a new list of the same three integers, sorted in ascending order.
# Ex:
#   sortThreeNumberAscending([1, 3, 2]) # return [1, 2, 3]
#   sortThreeNumberAscending([2, 1, 3]) # return [1, 2, 3]
from typing import List

def sortThreeNumberAscending(lst: List[int]) -> List[int]:
    if lst[0] > lst[1]:
        lst[0], lst[1] = lst[1], lst[0]

    if lst[0] > lst[2]:
        lst[0], lst[2] = lst[2], lst[0]

    if lst[1] > lst[2]:
        lst[1], lst[2] = lst[2], lst[1]

    return lst
