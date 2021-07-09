# Given a matrix of integers A of size N x M consisting of 0 and 1.
# A group of connected 1's forms an island. From a cell (i, j)
# such that A[i][j] = 1 you can visit any cell that shares a corner with (i, j)
# and value in that cell is 1.
# More formally, from any cell (i, j) if A[i][j] = 1 you can visit:
# (i-1, j) if (i-1, j) is inside the matrix and A[i-1][j] = 1.
# (i, j-1) if (i, j-1) is inside the matrix and A[i][j-1] = 1.
# (i+1, j) if (i+1, j) is inside the matrix and A[i+1][j] = 1.
# (i, j+1) if (i, j+1) is inside the matrix and A[i][j+1] = 1.
# (i-1, j-1) if (i-1, j-1) is inside the matrix and A[i-1][j-1] = 1.
# (i+1, j+1) if (i+1, j+1) is inside the matrix and A[i+1][j+1] = 1.
# (i-1, j+1) if (i-1, j+1) is inside the matrix and A[i-1][j+1] = 1.
# (i+1, j-1) if (i+1, j-1) is inside the matrix and A[i+1][j-1] = 1.
# Return the number of islands.
# NOTE: Rows are numbered from top to bottom and columns are numbered from left to right.
# 1 <= N, M <= 100
# 0 <= A[i] <= 1
# The only argument given is the integer matrix A.
# Return the number of islands.
import sys
sys.setrecursionlimit(10**8)


class Solution:
    moves = [(-1, 0), (0, -1), (1, 0), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]

    def util(self, A, x, y):
        A[x][y] = 0

        for dRow, dCol in Solution.moves:
            row = x + dRow
            col = y + dCol

            if 0 <= row < len(A) and 0 <= col < len(A[0]) and A[row][col] == 1:
                self.util(A, row, col)

    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        result = 0

        for m in range(len(A)):
            for n in range(len(A[0])):
                if A[m][n] == 1:
                    self.util(A, m, n)
                    result += 1

        return result


sol = Solution()
print(sol.solve([[0, 1, 0], [0, 0, 1], [1, 0, 0]]))  # 2
print(sol.solve([[1, 1, 0, 0, 0], [0, 1, 0, 0, 0], [1, 0, 0, 1, 1], [0, 0, 0, 0, 0], [1, 0, 1, 0, 1]]))  # 5
