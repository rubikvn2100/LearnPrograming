# Create a function that takes a list of integers as input.
# Return the largest number in the list.
# Ex:
#   getLargest([-9, -5, -2, -6, -3, -1]) # return -1
#   getLargest([3, 5, 7, -2, 6, -1, -3]) # return 7
from typing import List

def getLargest(lst: List[int]) -> int:
    lenLst = len(lst)

    i = 1
    largestNumber = lst[0]
    while i < lenLst:
        if lst[i] > largestNumber:
            largestNumber = lst[i]

        i = i + 1

    return largestNumber
