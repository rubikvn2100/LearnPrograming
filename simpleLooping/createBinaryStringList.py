# Create a function that takes an integer N as input.
# The function should return a list of binary strings.
# Where each string represents a binary value from 0 to N - 1 in ascending order.
# Ex:
#   createBinaryStringList(0) # return ["0"]
#   createBinaryStringList(2) # return ["0", "1"]
#   createBinaryStringList(4) # return ["0", "1", "10", "11"]
#   createBinaryStringList(6) # return ["0", "1", "10", "11", "100", "101"]
#   createBinaryStringList(8) # return ["0", "1", "10", "11", "100", "101", "110", "111"]
from typing import List

def createBinaryStringList(N: int) -> List[str]:
    if N <= 0:
        return []

    binaryStringList = ["0"]
    for num in range(1, N):
        binaryString = ""
        while num > 0:
            binaryString = ('1' if num % 2 else '0') + binaryString
            num >>= 1

        binaryStringList.append(binaryString)

    return binaryStringList
