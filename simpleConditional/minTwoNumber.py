# Note: In Python, there is a syntax shortcut that allows us to write a short conditional structure.
#       This is known as the ternary operator in other programming languages.
#       Here's an example of the ternary operator in Python:
#
#           def integerAbsoluteValue(n: int) -> int:
#               return -n if n < 0 else n
#
#           def dayInFebruary(year: int) -> int:
#               return 29 if year % 4 == 0 else 28
#
# Create a that takes two integers.
# Return the smaller number.
# Ex:
#   minTwoNumber(12, 3) # return 3
#   minTwoNumber(-2, 3) # return -2
def minTwoNumber(n1: int, n2: int) -> int:
    return n1 if n1 < n2 else n2
