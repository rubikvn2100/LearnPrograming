# Note: While humans use the base 10 numbering system, computers use base 2 (binary).
#       Despite their differences, both systems assign values to each place number.
#
#       base 10: 1011 = 1 * 10^0 + 1 * 10^1 + 0 * 10^2 + 1 * 10^3
#                     = 1 * 1    + 1 * 10   + 0 * 100  + 1 * 1000
#
#       base 2:  1011 = 1 *  2^0 + 1 *  2^1 + 0 *  2^2 + 1 *  2^3
#                     = 1 *  1   + 1 *  2   + 0 *  4   + 1 *  8
#                     = 11 (in base 10)
#
# Create a function that takes a list of integers as input.
# The integers represent a binary value, where each integer can only be 0 or 1.
# The function should convert the binary list into a string of binary digits, and return the string.
# If the input does not represent a binary list, return -1.
# Ex:
#   binaryListToString([1, 0, 1, 1])       # return "1101"
#   binaryListToString([0, 1, 1, 0, 0, 1]) # return "100110"
from typing import List

def binaryListToString(binaryList: List[int]) -> str:
    lenBinaryList = len(binaryList)

    if lenBinaryList == 0:
        return -1

    for digit in binaryList:
        if digit != 0 and digit != 1:
            return -1

    binaryString = ""
    for i in range(lenBinaryList):
        binaryString = ('1' if binaryList[i] else '0') + binaryString

    return binaryString
