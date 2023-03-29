# Note: "Increment" is an operation where we add 1 to the value of an integer.
#       When incrementing in base 10, if the place value is not the highest value, we will increase the place value by 1.
#       If the place value is already at the maximum value, we will set the place value back to 0 and carry 1 to the next place.
#
#       def increment(n: int) -> int:
#           return n + 1
#
#       print(increment(188)) # Display 189
#       print(increment(189)) # Display 190
#       print(increment(899)) # Display 900
#
# Create a function that takes a binary list as input.
# The function should return the binary list where the value is incremented by 1.
# The result list should have the same length as the input list.
# If the result contains more digits than the original input list, append the extra digit to the output list.
# If the input does not represent a binary list, return -1.
# Ex:
#   incrementBinaryList([1, 0, 0, 1]) # Return [0, 1, 0, 1]
#   incrementBinaryList([1, 1, 0, 1]) # Return [0, 0, 1, 1]
#   incrementBinaryList([1, 1, 1, 1]) # Return [0, 0, 0, 0, 1]
