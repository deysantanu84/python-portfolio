# We define f(X, Y) as number of different corresponding bits in binary representation of X and Y.
# For example, f(2, 7) = 2, since binary representation of 2 and 7 are 010 and 111, respectively.
# The first and the third bit differ, so f(2, 7) = 2.
# You are given an array of N positive integers, A1, A2 ,..., AN.
# Find sum of f(Ai, Aj) for all pairs (i, j) such that 1 ≤ i, j ≤ N. Return the answer modulo 10^9+7.
# 1 <= N <= 10^5
# 1 <= A[i] <= 2^31 - 1
def differentBitsSumPairwise(A):
    result = 0
    N = len(A)
    for i in range(31):
        setBitCount = 0
        for j in range(N):
            if A[j] & (1 << i):
                setBitCount += 1
        result = (result + setBitCount * (N - setBitCount) * 2) % (10**9 + 7)
    return result


print(differentBitsSumPairwise([1, 3, 5]))  # 8
# f(1, 1) + f(1, 3) + f(1, 5) + f(3, 1) + f(3, 3) + f(3, 5) + f(5, 1) + f(5, 3) + f(5, 5)
# = 0 + 1 + 1 + 1 + 0 + 2 + 1 + 2 + 0 = 8
print(differentBitsSumPairwise([2, 3]))  # 2
# f(2, 2) + f(2, 3) + f(3, 2) + f(3, 3) = 0 + 1 + 1 + 0 = 2
