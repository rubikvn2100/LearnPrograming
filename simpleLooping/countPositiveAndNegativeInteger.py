# Create a function that takes a list of integers as input.
# Return a tuple of two integers representing the count of positive and negative integers in the list, in that order.
# Ex:
#   countPositiveAndNegativeInteger([-9, -5, -2, -6, -3, -1]) # return (0, 6)
#   countPositiveAndNegativeInteger([3, 5, 7, -2, 6, -1, -3]) # return (4, 3)
from typing import List

def countPositiveAndNegativeInteger(lst: List[int]) -> int:
    lenLst = len(lst)

    i = 0
    countPositiveInteger = 0
    countNegativeInteger = 0
    while i < lenLst:
        if lst[i] > 0:
            countPositiveInteger = countPositiveInteger + 1

        if lst[i] < 0:
            countNegativeInteger = countNegativeInteger + 1

        i = i + 1

    return (countPositiveInteger, countNegativeInteger)
