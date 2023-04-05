# Create a function that takes a list of four integers as input.
# Return a new list of the same four integers, sorted in ascending order.
# Ex:
#   sortFourNumberAscending([2, 4, 1, 3]) # return [1, 2, 3, 4]
#   sortFourNumberAscending([3, 1, 4, 2]) # return [1, 2, 3, 4]
from typing import List

def sortFourNumberAscending(lst: List[int]) -> List[int]:
    if lst[0] > lst[1]:
        lst[0], lst[1] = lst[1], lst[0]

    if lst[2] > lst[3]:
        lst[2], lst[3] = lst[3], lst[2]

    if lst[0] > lst[2]:
        lst[0], lst[2] = lst[2], lst[0]

    if lst[1] > lst[3]:
        lst[1], lst[3] = lst[3], lst[1]

    if lst[1] > lst[2]:
        lst[1], lst[2] = lst[2], lst[1]

    return lst
