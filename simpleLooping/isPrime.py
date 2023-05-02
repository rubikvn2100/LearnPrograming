# Create a function that takes one integer as input.
# Return True if the input is a prime number, otherwise return False.
# Ex:
#   isPrime(937453153313) # return True
#   isPrime(965246846246) # return False
def isPrime(number: int) -> bool:
    if number < 2:
        return False

    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False

    return True
