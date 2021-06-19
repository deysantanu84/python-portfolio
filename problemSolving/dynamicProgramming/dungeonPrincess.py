# The demons had captured the princess and imprisoned her in the bottom-right corner of a dungeon.
# The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight was initially
# positioned in the top-left room and must fight his way through the dungeon to rescue the princess.
# The knight has an initial health point represented by a positive integer. If at any point his
# health point drops to 0 or below, he dies immediately.
# Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon
# entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase
# the knight's health (positive integers).
# In order to reach the princess as quickly as possible, the knight decides to move only
# rightward or downward in each step.
# Given a 2D array of integers A of size M x N. Find and return the knight's minimum initial
# health so that he is able to rescue the princess.
# 1 <= M, N <= 500
# -100 <= A[i] <= 100
# First and only argument is a 2D integer array A denoting the grid of size M x N.
# Return an integer denoting the knight's minimum initial health so that he is able to rescue the princess.
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def calculateMinimumHP(self, A):
        rows = len(A)
        columns = len(A[0])
        resultGrid = [[0] * columns for _ in range(rows)]

        resultGrid[-1][-1] = max(1, 1 - A[-1][-1])

        for i in range(rows - 2, -1, -1):
            resultGrid[i][-1] = max(1, resultGrid[i + 1][-1] - A[i][-1])

        for j in range(columns - 2, -1, -1):
            resultGrid[-1][j] = max(1, resultGrid[-1][j + 1] - A[-1][j])

        for i in range(rows - 2, -1, -1):
            for j in range(columns - 2, -1, -1):
                resultGrid[i][j] = max(1, min(resultGrid[i + 1][j] - A[i][j],
                                              resultGrid[i][j + 1] - A[i][j]))

        return resultGrid[0][0]


sol = Solution()
print(sol.calculateMinimumHP([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]))  # 7
print(sol.calculateMinimumHP([[1, -1, 0], [-1, 1, -1], [1, 0, -1]]))  # 1
