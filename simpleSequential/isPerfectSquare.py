# Note: A perfect square is an integer that is the product of another integer multiplied by itself.
#         Ex:
#           x = 16 is a perfect square because there is an integer y = 4 such that x = y^2
#           x = 25 is a perfect square because there is an integer y = 5 such that x = y^2
#       In other words, x is not a perfect square if there is not integer y such that x = y^2
#         Ex:
#           x = 17 is not a perfect square because there is no integer y such that x = y^2
#
# Create a function that take one integer variable.
# Return True if the input integer is a perfect square, otherwise return False.
# Hint: This problem can be done by combine multiple simple operators.
# Ex:
#   isPerfectSquare(16) # return True
#   isPerfectSquare(17) # return False
def isPerfectSquare(n: int) -> bool:
    return n >= 0 and int(n ** 0.5) ** 2 == n