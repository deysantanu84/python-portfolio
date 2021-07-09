# Given a matrix of integers A of size N x M consisting of 0 or 1.
# For each cell of the matrix find the distance of nearest 1 in the matrix.
# Distance between two cells (x1, y1) and (x2, y2) is defined as |x1 - x2| + |y1 - y2|.
# Find and return a matrix B of size N x M which defines for each cell in A
# distance of nearest 1 in the matrix A.
# NOTE: There is atleast one 1 is present in the matrix.
# 1 <= N, M <= 1000
# 0 <= A[i][j] <= 1
# The first argument given is the integer matrix A.
# Return the matrix B.
# TLE
import sys
INT_MAX = sys.maxsize


class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        rowCount = len(A)
        colCount = len(A[0])
        newX = [-1, 0, 1, 0]
        newY = [0, -1, 0, 1]
        queue = []
        resultGrid = [[0 for _ in range(colCount)] for _ in range(rowCount)]

        for i in range(rowCount):
            for j in range(colCount):
                resultGrid[i][j] = INT_MAX
                if A[i][j] == 1:
                    resultGrid[i][j] = 0
                    queue.append([i, j])

        while len(queue):
            popped = queue.pop(0)

            x = popped[0]
            y = popped[1]

            for i in range(4):
                adjX = x + newX[i]
                adjY = y + newY[i]

                if 0 <= adjX < rowCount and 0 <= adjY < colCount \
                        and resultGrid[adjX][adjY] > resultGrid[x][y] + 1:
                    resultGrid[adjX][adjY] = resultGrid[x][y] + 1
                    queue.append([adjX, adjY])

        return resultGrid


sol = Solution()
print(sol.solve([[0, 0, 0, 1], [0, 0, 1, 1], [0, 1, 1, 0]]))
# [[3, 2, 1, 0], [2, 1, 0, 0], [1, 0, 0, 1]]

print(sol.solve([[1, 0, 0], [0, 0, 0], [0, 0, 0]]))
# [[0, 1, 2], [1, 2, 3], [2, 3, 4]]
