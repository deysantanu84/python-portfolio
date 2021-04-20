# Reverse the bits of an 32 bit unsigned integer A.
def solve(A):
    result = 0
    for i in range(32):
        result <<= 1
        if A & 1 == 1:
            result ^= 1
        A >>= 1
    return result


print(solve(0))
print(solve(3))
print(solve(11))
