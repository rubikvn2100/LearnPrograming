# Create a function that takes two integers as input.
# Return the Greatest Common Divisor of them using Euclidean algorithm.
# Return -1 if both input are zeros as GCD(0, 0) is undefined.
# Ex:
#   twoNumberGreatestCommonDivisor(163, 0) # return 163
#   twoNumberGreatestCommonDivisor(24, 36) # return 12
#   twoNumberGreatestCommonDivisor(-6, 12) # return 6
#   twoNumberGreatestCommonDivisor(-6, -3) # return 3
def twoNumberGreatestCommonDivisor(num1: int, num2: int) -> int:
    if num1 == 0 and num2 == 0:
        return -1

    if num1 < 0:
        num1 = -num1

    if num2 < 0:
        num2 = -num2

    if num1 < num2:
       num1, num2 = num2, num1

    r = num1 % num2
    while r != 0:
        num1, num2 = num2, r
        r = num1 % num2

    return num2
