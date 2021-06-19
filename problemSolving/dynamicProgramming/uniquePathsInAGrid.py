# Given a grid of size n * m, lets assume you are starting at (1,1) and your goal is to reach (n, m).
# At any instance, if you are on (x, y), you can either go to (x, y + 1) or (x + 1, y).
# Now consider if some obstacles are added to the grids. How many unique paths would there be?
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
# 1 <= n, m <= 100
# A[i][j] = 0 or 1
# First and only argument A is a 2D array of size n * m.
# Return an integer denoting the number of unique paths from (1, 1) to (n, m).
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def uniquePathsWithObstacles(self, A):
        validPos = lambda m, n: (1 - A[n][m])

        height = len(A)
        width = len(A[0])

        if height * width == 0 or not validPos(0, 0):
            return 0

        A[0][0] = 1

        for y in range(1, height):
            A[y][0] = A[y - 1][0] * validPos(0, y)

        for x in range(1, width):
            A[0][x] = A[0][x - 1] * validPos(x, 0)

        for y in range(1, height):
            for x in range(1, width):
                A[y][x] = (A[y][x - 1] + A[y - 1][x]) * validPos(x, y)

        return A[height - 1][width - 1]


sol = Solution()
print(sol.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))  # 2
print(sol.uniquePathsWithObstacles([[0, 0, 0], [1, 1, 1], [0, 0, 0]]))  # 0
