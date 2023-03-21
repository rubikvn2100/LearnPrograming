# Note: In Python, a list is an ordered, mutable collection of elements enclosed in square brackets [].
#       A list can contain any number of elements, which can be of different data types,
#       and the elements are separated by commas.
#         Ex:
#           print([2])       # Displayed [2]
#           print([2, 3])    # Displayed [2, 3]
#           print([2, 3, 5]) # Displayed [2, 4, 5]
#
# Create a function that take an input `coordinate` which is a tuple of two integers.
# Return a list of four tuple of two integers that represent the neighbor coordinates of the input.
# The order of the coordinates should match the example.
# Ex:
#   listFourNeighborCoordinate((5, 6))   # return [(5, 7), (5, 5), (6, 6), (4, 6)]
#   listFourNeighborCoordinate((-2, -3)) # return [(-2, -2), (-2, -4], (-1, -3), (-3, -3)]
from typing import List, Tuple

def listFourNeighborCoordinate(coordinate:Tuple[int, int]) -> List[Tuple[int, int]]:
    x, y = coordinate
    return [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]