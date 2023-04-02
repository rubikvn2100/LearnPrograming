# Create a function that takes a list of integers as input.
# Return the smallest number in the list.
# Ex:
#   getSmallest([-9, -5, -2, -6, -3, -1]) # return -9
#   getSmallest([3, 5, 7, -2, 6, -1, -3]) # return -3
from typing import List

def getSmallest(lst: List[int]) -> int:
    lenLst = len(lst)

    i = 1
    smallestNumber = lst[0]
    while i < lenLst:
        if lst[i] < smallestNumber:
            smallestNumber = lst[i]

        i = i + 1

    return smallestNumber
