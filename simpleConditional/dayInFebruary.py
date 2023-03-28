# Note: Conditional structure allow a program to execute one of two available code blocks based on some boolean expression.
#       When using them in a function, a simple conditional structure is:
#       def foo(n):
#           if <boolean expression base on n>:
#               return <expression 1>
#
#           return <expression 2>
#
# Create a function that takes an integer representing a year as input and returns the number of days in February.
# Ex:
#   dayInFebruary(2023) # return 28
#   dayInFebruary(2024) # return 29
def dayInFebruary(year: int) -> int:
    if year % 4 == 0:
        return 29

    return 28