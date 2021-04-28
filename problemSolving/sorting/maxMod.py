# Given an array A of size N, groot wants you to pick 2 indices i and j such that
# 1 <= i, j <= N
# A[i] % A[j] is maximum among all possible pairs of (i, j).
# Help Groot in finding the maximum value of A[i] % A[j] for some i, j.
# 1 <= N <= 100000
# 0 <= A[i] <= 100000
import sys
INT_MIN = - sys.maxsize - 1


def maxMod(A):
    N = len(A)

    if N < 2:
        return 0

    maximum = INT_MIN
    secondMax = INT_MIN

    for i in range(N):
        if A[i] > maximum:
            secondMax = maximum
            maximum = A[i]

        elif A[i] > secondMax and A[i] != maximum:
            secondMax = A[i]

    if secondMax == INT_MIN:
        return 0

    else:
        return secondMax


print(maxMod([1, 2, 44, 3]))  # 3
print(maxMod([2, 6, 4]))  # 4
