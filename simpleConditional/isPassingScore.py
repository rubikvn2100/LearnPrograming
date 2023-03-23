# Note: Sometimes the input must be within a specific range. For example, a score cannot be below 0 or greater than 100.
#       We can specify this condition in the Application Program Interface (API) to inform the user.
#       However, mistakes can happen and the wrong number may be entered. In such cases, we need to validate the input.
#       We can use a simple validation mechanism as shown below:
#       def foo(n):
#           if <boolean expression that validates n>:
#               return -1
#
#           <rest of the code>
#
# Create a function that takes an integer representing a score.
# Return False if the score is below 60, otherwise return True.
# Return -1 if the input is below 0 or greater than 100.
# Ex:
#   isPassingScore(-9)  # return -1
#   isPassingScore(59)  # return False
#   isPassingScore(90)  # return True
#   isPassingScore(981) # return -1
