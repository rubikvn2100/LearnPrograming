# Note: Recursion is a programming technique where a function calls itself to
#       solve a problem or perform a task. It's important to keep the main
#       recursive function clean while still including guarding conditions to
#       sanitize bad data. By storing data in a memoization table that we can
#       look up later, we can even speed up the process. Sometimes, when
#       solving a child problem, it's necessary to access the previous choice
#       made in the parent problem.
#
#           def recursionFunction(<parameters>) -> <return type>:
#               <guarding conditions>
#
#               previousChoice = <default value>
#               <memoization table initialization>
#               def recursionFunctionHelper(<parameters>) -> <return type>:
#                   <lookup case>
#
#                   <Base case>
#
#                   <Recursive case base on previous choice>
#
#               return recursionFunctionHelper(<parameters>)
#
# Create a that takes one integer sum.
# Return the number of non descending ordered list of non negative integer that add up to sum.
# Ex:
#   countNonDescendingOrderedAdditionOfSum(5) # return 7
#   countNonDescendingOrderedAdditionOfSum(9) # return 30
#
# Explanation:
#   When sum = 5, the lists that have sum add up to 4 non descending ordered are:
#     5 = 1 + 1 + 1 + 1 + 1
#     5 = 1 + 1 + 1 + 2
#     5 = 1 + 1 + 3
#     5 = 1 + 2 + 2
#     5 = 1 + 4
#     5 = 2 + 3
#     5 = 5
