# Create a function that takes an integer N.
# Return the sum of the squares of all positive integers that are less than N.
# If the input is less than 0, return -1.
# Ex:
#   sumIntegerSquareToN(-100000) # return -1
#   sumIntegerSquareToN(3)       # return 5
#   sumIntegerSquareToN(1234567) # return 627223338685887771
def sumIntegerSquareToN(n: int) -> int:
    if n < 0:
        return -1
    
    i = 1
    total = 0
    while i < n:
        total = total + i ** 2
        
        i = i + 1
    
    return total
