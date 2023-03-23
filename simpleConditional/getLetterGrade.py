# Note: Simple conditions allow us to make decisions between two code blocks.
#       However, sometimes we need to make multiple decisions that are related to each other.
#       In such cases, we can use an if-else-if structure as follows:
#       def foo(n):
#           if <boolean expression 1 base on n>:
#               return <expression 1>
#           elif <boolean expression 2 base on n>:
#               return <expression 2>
#           elif <boolean expression 3 base on n>:
#               return <expression 3>
#           else:
#               return <expression 4>
#
#           return <expression 5>
#
# Create a function that takes an integer representing a score.
# Return letter grade where:
#   A: 90 <= score
#   B: 80 <= score < 70
#   C: 70 <= score < 60
#   D: 60 <= score < 50
#   F:       score < 60
# Return -1 if the input is below 0 or greater than 100.
# Ex:
#   getLetterGrade(-9)  # return -1
#   getLetterGrade(59)  # return 'F'
#   getLetterGrade(90)  # return 'A'
#   getLetterGrade(981) # return -1
