# Create a function that takes a list of five integers as an input.
# Return a new list containing the square of each integer in the original list.
# Ex:
#   squareFiveIntegerList([-2, -1, 0, 1, 2]) # return [4, 1, 0, 1, 4]
#   squareFiveIntegerList([3, 5, 9, -2, -7]) # return [9, 25, 81, 4, 49]
from typing import List

def squareFiveIntegerList(lst: List[int]) -> List[int]:
    return ([lst[0] ** 2, lst[1] ** 2, lst[2] ** 2, lst[3] ** 2, lst[4] ** 2])