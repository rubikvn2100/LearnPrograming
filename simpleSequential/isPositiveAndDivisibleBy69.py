# Note: `<`, `>`, `<=`, `>=`, `==`, `!=` are comparison operators that return boolean.
#       A boolean expression is an expression that use comparision operators list above. Ex: `a == 2`
#       A complex boolean expression invole multiple boolean expression that can be link using
#         `logical operators` such as `and`, `or`, and `not`
# Ex:
#   a % 2 == 0 and a % 3 == 0 # return True if a is divisible by 2 and 3.
#   not(a < 0 or a > 10)      # return True if a is in [0, 10] inclusive.
#
# Create a function that take one integer number and return True if it is positive an divisible by 69, otherwise return False.
# This function is simple and you will not need to use condition structure.
# Ex:
#   isPositiveAndDivisibleBy69(690) # return True
#   isPositiveAndDivisibleBy69(-69) # return False
def isPositiveAndDivisibleBy69(var: int) -> bool:
    return var > 0 and var % 69 == 0
