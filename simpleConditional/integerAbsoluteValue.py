# Note: Conditional structure allow a program to execute one of two available code blocks based on some boolean expression.
#       When using them in a function, a simple conditional structure is:
#       def foo(n):
#           if <boolean expression base on n>:
#               return <expression 1>
#
#           return <expression 2>
#
# Create a function that takes an integer as input and returns its absolute value.
# Ex:
#   integerAbsoluteValue(13) # return 13
#   integerAbsoluteValue(0)  # return 0
#   integerAbsoluteValue(-2) # return 2
def integerAbsoluteValue(n: int) -> int:
    if n < 0:
        return -n

    return n