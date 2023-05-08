# Note: Recursion is a programming technique where a function calls itself to
#       solve a problem or perform a task. Sometimes, when solving a child
#       problem, it's necessary to access the previous choice made in the
#       parent problem. However, when the recursion function is called for
#       the first time, there may be no previous choice to access. In such
#       cases, you can use a specific recursion structure that provides a
#       default value to handle such scenarios.
#
#           def recursionFunction(state: <state type>, previousChoice: <choice type> = <default value>) -> <return type>:
#               <Base case>
#
#               <Recursive case base on previous choice>
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
