# Note: For the purpose of improving your programming skills,
#       please refrain from using the built-in sum() function.
#
# Create a function that takes a list of five integers as an input.
# Return the sum of the numbers in the list.
# Ex:
#   sumFiveIntegerList([-5, -3, 2, 6, 0]) # return 0
#   sumFiveIntegerList([1, 5, 2, 4, 3])   # return 15
from typing import List

def sumFiveIntegerList(lst: List[int]) -> int:
    return (lst[0] + lst[1] + lst[2] + lst[3] + lst[4])