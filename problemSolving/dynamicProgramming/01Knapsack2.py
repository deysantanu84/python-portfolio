# Given two integer arrays A and B of size N each which represent
# values and weights associated with N items respectively.
# Also given an integer C which represents knapsack capacity.
# Find out the maximum value subset of A such that sum of the weights of this subset
# is smaller than or equal to C.
# NOTE:
# You cannot break an item, either pick the complete item, or don’t pick it (0-1 property).
# 1 <= N <= 500
# 1 <= C, B[i] <= 10^6
# 1 <= A[i] <= 50
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
        resultList = [0 for _ in range(C + 1)]

        for i in range(1, N + 1):
            for j in range(C, 0, -1):
                if B[i - 1] <= j:
                    resultList[j] = max(resultList[j],
                                        resultList[j - B[i - 1]] + A[i - 1])

        return resultList[C]


sol = Solution()
print(sol.solve([6, 10, 12], [10, 20, 30], 50))  # 22
print(sol.solve([1, 2, 3, 4], [12, 13, 15, 19], 10))  # 0
