# Create a function that takes a string as input.
# Return True if the input string has one or more spaces at the end, and False otherwise.
# Ex:
#   hasSpaceAtEnd("")                  # return False
#   hasSpaceAtEnd("Hello  World!")     # return False
#   hasSpaceAtEnd("  Hello  World!  ") # return True
from typing import List

def hasSpaceAtEnd(s: str) -> bool:
    return len(s) > 0 and s[-1] == ' '
