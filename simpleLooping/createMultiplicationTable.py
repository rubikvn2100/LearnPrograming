# Note: Up until this point, we have been using a simple list of primitive values as a one-dimensional array.
#       However, we can also use a list of lists of integers to represent a two-dimensional array.
#       Where each inner list represents a row in the array.
#
#         matrix = [[1, 2, 3], [4, 5, 6]]
#
#       We can imagine this as a table with 2 rows and 3 columns:
#
#         matrix = [[1, 2, 3],
#                   [4, 5, 6]]
#
# Create a function that takes two integers, N and M, as input.
# The function should return a list of lists of integers.
# Where each inner list represents a row of the multiplication table from 1 to N, up to the Mth column.
# Ex:
#   createMultiplicationTable(3, 4) # returns [[1, 2, 3, 4], [2, 4, 6, 8], [3, 6, 9, 12]]
#   createMultiplicationTable(2, 5) # returns [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10]]
from typing import List

def createMultiplicationTable(N: int, M: int) -> List[List[int]]:
    return [[i * j for j in range(1, M + 1)] for i in range(1, N + 1)]
