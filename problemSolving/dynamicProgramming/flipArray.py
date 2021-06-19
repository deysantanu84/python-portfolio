# Given an array A of positive elements, you have to flip the sign of some of its elements
# such that the resultant sum of the elements of array should be minimum non-negative
# (as close to zero as possible).
# Return the minimum number of elements whose sign needs to be flipped such that the
# resultant sum is minimum non-negative.
# 1 <= length of(A) <= 100
# Sum of all the elements will not exceed 10,000.
# First and only argument is an integer array A.
# Return an integer denoting the minimum number of elements whose sign needs to be flipped.
import sys
INT_MAX = sys.maxsize - 1


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def solve(self, A):
        P = sum(A) // 2 + 1
        Q = len(A) + 1

        resultGrid = [[i and INT_MAX or 0] * Q for i in range(P)]

        for i in range(P):
            for j in range(1, Q):
                if i - A[j - 1] >= 0:
                    resultGrid[i][j] = min(resultGrid[i][j - 1],
                                           resultGrid[i - A[j - 1]][j - 1] + 1)
                else:
                    resultGrid[i][j] = resultGrid[i][j - 1]

        for row in resultGrid[::-1]:
            if row[-1] < INT_MAX:
                return row[-1]


sol = Solution()
print(sol.solve([15, 10, 6]))  # 1
print(sol.solve([14, 10, 4]))  # 1
