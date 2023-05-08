# Note: Recursion is a programming technique where a function calls itself to
#       solve a problem or perform a task. Recursion use to have the following structure:
#
#           def recursionFunction(<parameters>) -> <return type>:
#               <Base Case>
#
#               <Recursive Case>
#
# Create a that takes one non negative integer.
# Return the fibonacci of that number.
# Return -1 if the input is negative.
# Ex:
#   fibonacci(10) # return 55
#   fibonacci(12) # return 144
def fibonacci(number: int) -> int:
    if number < 0:
        return -1

    if number <= 1:
        return number

    return fibonacci(number - 1) + fibonacci(number - 2)
