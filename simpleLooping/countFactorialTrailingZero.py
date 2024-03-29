# Create a function that takes an integer N as input.
# Return the number of trailing zero of N factorial.
# Ex:
#   countFactorialTrailingZero(7)             # return 1
#   countFactorialTrailingZero(12)            # return 2
#   countFactorialTrailingZero(183)           # return 44
#   countFactorialTrailingZero(343118)        # return 85773
#   countFactorialTrailingZero(722935669)     # return 180733910
#   countFactorialTrailingZero(525242356355)  # return 131310589082
def countFactorialTrailingZero(N: int) -> int:
    if N < 5:
        return 0

    numOfTraillingZero = 0
    powerOfFive = 5
    while powerOfFive < N:
        numOfTraillingZero += N // powerOfFive
        powerOfFive *= 5

    return numOfTraillingZero
