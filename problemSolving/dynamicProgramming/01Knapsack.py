# Given two integer arrays A and B of size N each which represent
# values and weights associated with N items respectively.
# Also given an integer C which represents knapsack capacity.
# Find out the maximum value subset of A such that sum of the weights of this subset
# is smaller than or equal to C.
# NOTE:
# You cannot break an item, either pick the complete item, or don’t pick it (0-1 property).
# 1 <= N <= 10^3
# 1 <= C <= 10^3
# 1 <= A[i], B[i] <= 10^3
# First argument is an integer array A of size N denoting the values on N items.
# Second argument is an integer array B of size N denoting the weights on N items.
# Third argument is an integer C denoting the knapsack capacity.
# Return a single integer denoting the maximum value subset of A
# such that sum of the weights of this subset is smaller than or equal to C.
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        N = len(A)
        resultGrid = [[0 for _ in range(C + 1)] for _ in range(N + 1)]

        for i in range(N + 1):
            for j in range(C + 1):
                if i == 0 or j == 0:
                    resultGrid[i][j] = 0

                elif B[i - 1] <= j:
                    resultGrid[i][j] = max(A[i - 1] + resultGrid[i - 1][j - B[i - 1]],
                                           resultGrid[i - 1][j])

                else:
                    resultGrid[i][j] = resultGrid[i - 1][j]

        return resultGrid[N][C]


sol = Solution()
print(sol.solve([60, 100, 120], [10, 20, 30], 50))  # 220
print(sol.solve([10, 20, 30, 40], [12, 13, 15, 19], 10))  # 0
