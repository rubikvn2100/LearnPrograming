# Note: In Python, we can use slicing to get a sublist of a list or string.
#       For example, to get a sublist of a list without the last two elements:
#
#         lst = [2, 3, 5, 7, 11]
#         subList = lst[:-2] # Note: lst[:3] aslo work, but we need to know the cut off index is 3.
#         print(subList) # Display [2, 3, 5]
#
#       Similarly, to get a sublist of a string without the last two characters:
#
#         str = "Python"
#         subStr = str[:-2] # Note: lst[:4] aslo work, but we need to know the cut off index is 4.
#         print(subStr) # Display "Pyth"
#
# Create a function that takes a string as input.
# Remove all spaces in the end of the list.
# Ex:
#   removeSpaceAtEnd("")                  # return ""
#   removeSpaceAtEnd("Hello  World!")     # return "Hello  World!"
#   removeSpaceAtEnd("  Hello  World!  ") # return "  Hello  World!"
from typing import List

def removeSpaceAtEnd(s: str) -> str:
    i = len(s) - 1
    while i >= 0 and s[i] == ' ':
        i = i - 1

    return s[:i + 1]
