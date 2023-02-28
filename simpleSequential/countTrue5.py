# Note: True and False are just a human readable representation of boolean type. Behind the screen, it is interger.
#       If you use boolean in an expression, you will see that in Python, True is 1 and False is 0.
# Ex:
#   print(True)                # True
#   print(True + False + True) # 2
#   print((True + True) * 420) # 840
#   print((False + True) * 69) # 69
#
# Create a function that take five boolean values. Return the number of True arguments.
# This function is simple and you will not need to use condition structure.
# Ex: 
#   countTrue5(True, False, True, False, False) return 2
#   countTrue5(True, True, True, False, False)  return 3
def countTrue5(bool1: bool, bool2: bool, bool3: bool, bool4: bool, bool5: bool) -> int:
    return bool1 + bool2 + bool3 + bool4 + bool5
