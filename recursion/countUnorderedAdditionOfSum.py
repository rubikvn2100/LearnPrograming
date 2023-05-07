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
# Create a that takes one integer sum.
# Return the number of unordered list of non negative integer that add up to sum.
# Ex:
#   countUnorderedAdditionOfSum(4) # return 8
#   countUnorderedAdditionOfSum(9) # return 256
#
# Explanation:
#   When sum = 4, the list that have sum add up to 4 unordered are:
#     4 = 1 + 1 + 1 + 1
#     4 = 1 + 1 + 2
#     4 = 1 + 2 + 1
#     4 = 1 + 3
#     4 = 2 + 1 + 1
#     4 = 2 + 2
#     4 = 3 + 1
#     4 = 4
