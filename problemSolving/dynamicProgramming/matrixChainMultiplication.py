# Given an array of integers A representing chain of 2-D matrices
# such that the dimensions of ith matrix is A[i-1] x A[i].
# Find the most efficient way to multiply these matrices together.
# The problem is not actually to perform the multiplications,
# but merely to decide in which order to perform the multiplications.
# Return the minimum number of multiplications needed to multiply the chain.
# 1 <= length of the array <= 1000
# 1 <= A[i] <= 100
# The only argument given is the integer array A.
# Return an integer denoting the minimum number of multiplications needed to multiply the chain.
import sys
INT_MAX = sys.maxsize


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        N = len(A)
        resultGrid = [[0 for _ in range(N)] for _ in range(N)]

        for i in range(1, N):
            resultGrid[i][i] = 0

        for length in range(2, N):
            for m in range(1, N - length + 1):
                n = m + length - 1
                resultGrid[m][n] = INT_MAX

                for p in range(m, n):
                    q = resultGrid[m][p] + resultGrid[p + 1][n] + A[m-1] * A[p] * A[n]

                    if q < resultGrid[m][n]:
                        resultGrid[m][n] = q

        return resultGrid[1][-1]


sol = Solution()
print(sol.solve([40, 20, 30, 10, 30]))  # 26000
print(sol.solve([10, 20, 30]))  # 6000
