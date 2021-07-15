# You are given a read only array of n integers from 1 to n.
# Each integer appears exactly once except A which appears twice and B which is missing.
# Return A and B.
# Note: Your algorithm should have a linear runtime complexity.
# Could you implement it without using extra memory?
# Note that in your output A should precede B.
def repeatAndMissingNumber(A):
    result = []
    N = len(A)
    sum1ToN = (N * (N + 1)) // 2
    sum1ToNSquared = ((N * (N + 1) * (2 * N + 1)) // 6)

    for i in range(N):
        sum1ToN -= A[i]
        sum1ToNSquared -= A[i] * A[i]

    missing = (sum1ToN + sum1ToNSquared // sum1ToN) // 2
    repeating = missing - sum1ToN
    result.append(repeating)
    result.append(missing)
    return result


print(repeatAndMissingNumber([4, 3, 6, 2, 1, 6, 7]))  # [6, 5]
print(repeatAndMissingNumber([3, 1, 2, 5, 3]))  # [3, 4]
