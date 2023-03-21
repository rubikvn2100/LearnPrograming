# Note: In Python, a tuple is an ordered, immutable collection of elements enclosed in parentheses `()`.
#       A tuple can contain any number of elements, which can be of different data types,
#       and the elements are separated by commas.
#         Ex:
#           print((2))       # Displayed (2)
#           print((2, 3))    # Displayed (2, 3)
#           print((2, 3, 5)) # Displayed (2, 3, 5)
#
# We want to represent coordinate with a pair of variable `x`, `y`.
# But, we don't want to carry them seperately because they lose their meaning when sepearte.
#
# Create a function that take two integer variables `x` and `y`.
# Return a tuple `(x, y)` which represent the coordinate.
# Ex:
#   makeCoordinateTuple(10, 1) # return (10, 1)
#   makeCoordinateTuple(-5, 3) # return (-5, 3)
from typing import Tuple

def makeCoordinateTuple(x: int, y: int) -> Tuple[int, int]:
    return (x, y)