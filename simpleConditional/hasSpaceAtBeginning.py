# Create a function that takes a string as input.
# Return True if the input string has one or more spaces at the beginning, and False otherwise.
# Ex:
#   hasSpaceAtBeginning("")                  # return False
#   hasSpaceAtBeginning("Hello  World!")     # return False
#   hasSpaceAtBeginning("  Hello  World!  ") # return True
from typing import List

def hasSpaceAtBeginning(s: str) -> bool:
    return len(s) > 0 and s[0] == ' '
