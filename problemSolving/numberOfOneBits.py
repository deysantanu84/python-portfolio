# Write a function that takes an unsigned integer and returns the number of 1 bits it has.
def solve(A):
    result = 0
    while A:
        result += A & 1
        A >>= 1
    return result


solve(11)
