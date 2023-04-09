# Note: In Python, we can use slicing to get a sublist of a list or string.
#       For example, to get a sublist of a list without the first two elements:
#
#         lst = [2, 3, 5, 7, 11]
#         subList = lst[2:]
#         print(subList) # Display [5, 7, 11]
#
#       Similarly, to get a sublist of a string without the first two characters:
#
#         str = "Python"
#         subStr = str[2:]
#         print(subStr) # Display "thon"
#
# Create a function that takes a string as input.
# Remove all spaces in the front of the list.
# Ex:
#   removeSpaceAtBeginning("")                  # return ""
#   removeSpaceAtBeginning("Hello  World!")     # return "Hello  World!"
#   removeSpaceAtBeginning("  Hello  World!  ") # return "Hello  World!  "
from typing import List

def removeSpaceAtBeginning(s: str) -> str:
    i = 0
    while i < len(s) and s[i] == ' ':
        i = i + 1

    return s[i:]
