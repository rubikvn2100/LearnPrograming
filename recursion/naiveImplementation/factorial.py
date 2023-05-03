# Note: Recursion is a programming technique where a function calls itself to
#       solve a problem or perform a task. Recursion use to have the following structure:
#
#           def recursionFunction(<parameters>) -> <return type>:
#               <Base Case>
#
#               <Recursive Case>
#
# Create a that takes one non negative integer.
# Return the factorial of that number.
# Return -1 if the input is negative.
# Ex:
#   factorial(5) # return 120
#   factorial(6) # return 720
def factorial(number: int) -> int:
    if number < 0:
        return -1

    if number == 0:
        return 1

    return number * factorial(number - 1)
