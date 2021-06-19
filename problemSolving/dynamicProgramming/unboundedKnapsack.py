# Given a knapsack weight A and a set of items with certain value B[i] and weight C[i],
# we need to calculate maximum amount that could fit in this quantity.
# This is different from classical Knapsack problem, here we are allowed to use
# unlimited number of instances of an item.
# 1 <= A <= 1000
# 1 <= |B| <= 1000
# 1 <= B[i] <= 1000
# 1 <= C[i] <= 1000
# First argument is the Weight of knapsack A
# Second argument is the vector of values B
# Third argument is the vector of weights C
# Return the maximum value that fills the knapsack completely
class Solution:
    # @param A : integer
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        N = len(B)
        resultList = [0 for _ in range(A + 1)]

        for i in range(A + 1):
            for j in range(N):
                if C[j] <= i:
                    resultList[i] = max(resultList[i], resultList[i - C[j]] + B[j])

        return resultList[A]


sol = Solution()
print(sol.solve(10, [5], [10]))  # 5
print(sol.solve(10, [6, 7], [5, 5]))  # 14
