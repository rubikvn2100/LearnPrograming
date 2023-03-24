# Note: Looping structure allow a program to execute a code block repeatedly.
#       This structure has three important components:
#         1. Loop initialization: This is where the iterable is typically declared.
#         2. Loop control statement: This is where the iterable is involved in the decision-making process.
#         3. Loop body code block: This is where the iterable is typically updated.
#       The basic structure of a loop can be written as follows:
#       <loop initialization>
#       while <loop control statement>:
#           <code block>
#
#           <update iterable state>
#
# Create a function that takes an integer N and returns the sum of all positive integers that are less than N.
# If the input is less than 0, return -1.
# Ex:
#   sumIntegerToN(-1000000) # return -1
#   sumIntegerToN(3)        # return 3
#   sumIntegerToN(12345678) # return 76207876467003
