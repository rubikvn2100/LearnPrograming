# Create a function that takes a list of integers as input.
# Return the Greatest Common Divisor of them using Euclidean algorithm.
# Return -1 if at least two integers are zeros as GCD(0, 0) is undefined.
# Ex:
#   listGreatestCommonDivisor(-42, 402, -66, 354, 78, 426) # return 6
#   listGreatestCommonDivisor(7883933, 91928167, 54151651) # return 1
from typing import List

def gcdHelper(a: int, b: int) -> int:
    while b:
        a, b = b, a % b

    return a

def listGreatestCommonDivisor(integerList: List[int]) -> int:
    lenIntegerList = len(integerList)

    if lenIntegerList == 0:
        return -1

    if lenIntegerList == 1:
        return integerList[0]

    for i in range(lenIntegerList):
        if integerList[i] < 0:
            integerList[i] = -integerList[i]

    count = 0
    for num in integerList:
        if num == 0:
            count += 1

            if count >= 2:
                return - 1

    resultGCD= gcdHelper(integerList[0], integerList[1])
    for i in range(2, lenIntegerList):
        resultGCD = gcdHelper(resultGCD, integerList[i])

    return resultGCD
