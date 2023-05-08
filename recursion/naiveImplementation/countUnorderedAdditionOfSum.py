# Create a that takes one integer sum.
# Return the number of unordered list of non negative integer that add up to sum.
# Ex:
#   countUnorderedAdditionOfSum(4) # return 8
#   countUnorderedAdditionOfSum(9) # return 256
#
# Explanation:
#   When sum = 4, the list that have sum add up to 4 unordered are:
#     4 = 1 + 1 + 1 + 1
#     4 = 1 + 1 + 2
#     4 = 1 + 2 + 1
#     4 = 1 + 3
#     4 = 2 + 1 + 1
#     4 = 2 + 2
#     4 = 3 + 1
#     4 = 4
def countUnorderedAdditionOfSum(sum: int) -> int:
    if sum < 0:
        return 0

    if sum == 0:
        return 1

    count = 0
    for i in range(1, sum + 1):
        count += countUnorderedAdditionOfSum(sum - i)

    return count
