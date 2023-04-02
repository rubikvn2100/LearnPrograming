# Create a function that takes a list of integers as input.
# Return the number of positive integers in the list.
# Ex:
#   countPositiveInteger([-9, -5, -2, -6, -3, -1]) # return 0
#   countPositiveInteger([3, 5, 7, -2, 6, -1, -3]) # return 4
from typing import List

def countPositiveInteger(lst) -> int:
    lenLst = len(lst)
    
    i = 0
    count = 0
    while i < lenLst:
        if lst[i] > 0:
            count = count + 1
       
        i = i + 1
    
    return count