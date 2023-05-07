# Note: Recursion is a programming technique where a function calls itself to
#       solve a problem or perform a task. It's important to keep the main
#       recursive function clean while still including guarding conditions
#       to sanitize bad data.
#
#           def recursionFunction(<parameters>) -> <return type>:
#               <guarding conditions>
#
#               def recursionFunctionHelper(<parameters>) -> <return type>:
#                   <Base case>
#
#                   <Recursive case>
#
#               return recursionFunctionHelper(<parameters>)
#
# Create a that takes one non negative integer.
# Return the factorial of that number.
# Return -1 if the input is negative.
# Ex:
#   factorial(5) # return 120
#   factorial(6) # return 720
