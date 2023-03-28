# Note: In Python, we can use a list comprehension to create a list of integers.
#       The following code generates a list of integers from 0 to N - 1 in descending order:
#
#         N = 4
#         my_list = [N - i - 1 for i in range(N)]
#         print(my_list) # displays [3, 2, 1, 0]
#
# Create a function that takes two integers, base and power, as input.
# The function should return a list of power integers.
# Where each integer is a power of the base, from base ^ 0 to base ^ (power - 1).
# Ex:
#   createListPowerOfBase(2, 4) # returns [1, 2, 4, 8]
#   createListPowerOfBase(3, 3) # returns [1, 3, 9]
