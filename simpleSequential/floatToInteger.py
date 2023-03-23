# Note: Sometime we need to convert float to integer. It can be done using a build in function.
#       This can be use as a way to round down a float number.
#
# Create a function that take one float number.
# Return an integer which is the integer part of the input.
# Ex:
#   floatToInteger(0.012) # return 0
#   floatToInteger(1.234) # return 1
#   floatToInteger(123.4) # return 123
def floatToInteger(x: float) -> int:
    return int(x)