# Note: In Python, a list is an ordered, mutable collection of elements enclosed in square brackets [].
#       A list can contain any number of elements, which can be of different data types,
#       and the elements are separated by commas.
#         Ex:
#           print([2])       # Displayed [2]
#           print([2, 3])    # Displayed [2, 3]
#           print([2, 3, 5]) # Displayed [2, 4, 5]
#
# Create a function that take one integer variable.
# Return a list of the next five integer.
# Ex:
#   listNextFiveNumber(-3) # return [-2, -1, 0, 1, 2]
#   listNextFiveNumber(5)  # return [6, 7 8, 9, 10]
from typing import List

def listNextFiveNumber(n: int) -> List[int]:
    return [n + 1, n + 2, n + 3, n + 4, n + 5]