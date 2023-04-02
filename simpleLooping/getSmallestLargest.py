# Create a function that takes a list of integers as input.
# Return a tuple of two integers representing the smallest and largest values in the list, in that order.
# Ex:
#   countPositiveAndNegativeInteger([-9, -5, -2, -6, -3, -1]) # return (-9, -1)
#   countPositiveAndNegativeInteger([3, 5, 7, -2, 6, -1, -3]) # return (-3, 7)
from typing import List, Tuple

def getSmallestLargest(lst: List[int]) -> Tuple[int, int]:
    lenLst = len(lst)
    
    smallestNumber = lst[0]
    largestNumber = lst[0]
    i = 1
    while i < lenLst:
        if lst[i] < smallestNumber:
            smallestNumber = lst[i]

        if lst[i] > largestNumber:
            largestNumber = lst[i]
        
        i = i + 1

    return (smallestNumber, largestNumber)
