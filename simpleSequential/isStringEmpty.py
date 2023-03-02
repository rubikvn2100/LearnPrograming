# Note: Comparison operation can be use with string just as interger and boolean.
#       Comparison operation are `<`, `>`, `<=`, `>=`, `==`, `!=`
#
# Create a function that take one string, and return True if the string is empty, otherwise return False.
# This function is simple and you will not need to use condition structure.
# Ex:
#   isStringEmpty("")            # return True
#   isStringEmpty("Hello World") # return False
def isStringEmpty(var: str) -> bool:
    return var == ""