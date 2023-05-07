# Note: Recursion is a programming technique where a function calls itself to
#       solve a problem or perform a task. It's important to keep the main
#       recursive function clean while still including guarding conditions to
#       sanitize bad data. By storing data in a memoization table that we can
#       look up later, we can even speed up the process.
#
#           def recursionFunction(<parameters>) -> <return type>:
#               <guarding conditions>
#
#               <memoization table initialization>
#               def recursionFunctionHelper(<parameters>) -> <return type>:
#                   <lookup case>
#
#                   <Base case>
#
#                   <Recursive case>
#
#               return recursionFunctionHelper(<parameters>)
#
# Create a that takes one non negative integer.
# Return the fibonacci of that number.
# Return -1 if the input is negative.
# Ex:
#   fibonacci(10) # return 55
#   fibonacci(12) # return 144
