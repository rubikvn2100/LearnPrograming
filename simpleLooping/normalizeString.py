# Note: In Python, we can use slicing to get a sublist of a list or string.
#       For example, to get a sublist of a list without the first and last two elements:
#
#         lst = [2, 3, 5, 7, 11]
#         subList = lst[2:-2] # Note: lst[2:3] aslo work, but we need to know the cut off index is 3.
#         print(subList) # Display [5]
#
#       Similarly, to get a sublist of a string without the first and last two characters:
#
#         str = "Python"
#         subStr = str[2:-2] # Note: lst[2:4] aslo work, but we need to know the cut off index is 4.
#         print(subStr) # Display "th"
#
# Create a function that takes a string as input.
# Remove all spaces in the front and end of the list.
# Only one space is allow between two words.
# Ex:
#   normalizeString("")                  # return ""
#   normalizeString("Hello  World!")     # return "Hello World!"
#   normalizeString("  Hello  World!  ") # return "Hello World!"
from typing import List

def normalizeString(string: str) -> str:
    lenString = len(string)

    i = 0
    while i < lenString and string[i] == ' ':
        i += 1

    normalizedString = ''
    if i < lenString:
        normalizedString += string[i]
        i += 1

    while i < lenString:
        if string[i - 1] != ' ' or string[i] != ' ':
            normalizedString += string[i]
        i += 1

    if len(normalizedString) > 0 and normalizedString[-1] == ' ':
        return normalizedString[:-1]

    return normalizedString

