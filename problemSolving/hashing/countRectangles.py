# Given two arrays of integers A and B of size N each, where each pair (A[i], B[i])
# for 0 <= i < N represents a unique point (x, y) in 2-D Cartesian plane.
# Find and return the number of unordered quadruplet (i, j, k, l) such that
# (A[i], B[i]), (A[j], B[j]), (A[k], B[k]) and (A[l], B[l]) form a rectangle
# with the rectangle having all the sides parallel to either x-axis or y-axis.
# 1 <= N <= 2000
# 0 <= A[i], B[i] <= 10^9
# The first argument given is the integer array A.
# The second argument given is the integer array B.
# Return the number of unordered quadruplet that form a rectangle.
from collections import defaultdict


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        N = len(A)
        result = 0
        setDict = defaultdict(set)

        for i in range(N):
            setDict[A[i]].add((B[i]))

        for i in range(N - 1):
            for j in range(i + 1, N):
                if A[i] != A[j] and B[i] != B[j]:
                    if B[j] in setDict[A[i]] and B[i] in setDict[A[j]]:
                        result += 1

        return result // 2


sol = Solution()
print(sol.solve([1, 1, 2, 2], [1, 2, 1, 2]))  # 1
print(sol.solve([1, 1, 2, 2, 3, 3], [1, 2, 1, 2, 1, 2]))  # 3
