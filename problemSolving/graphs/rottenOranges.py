# Given a matrix of integers A of size N x M consisting of 0, 1 or 2.
# Each cell can have three values:
# The value 0 representing an empty cell.
# The value 1 representing a fresh orange.
# The value 2 representing a rotten orange.
# Every minute, any fresh orange that is adjacent (Left, Right, Top, or Bottom) to a rotten orange
# becomes rotten. Return the minimum number of minutes that must elapse until no cell has a fresh orange.
# If this is impossible, return -1 instead.
# Note: Your solution will run on multiple test cases.
# If you are using global variables, make sure to clear them.
# 1 <= N, M <= 1000
# 0 <= A[i][j] <= 2
# The first argument given is the integer matrix A.
# Return the minimum number of minutes that must elapse until no cell has a fresh orange.
# If this is impossible, return -1 instead.
class Solution:
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        result = 0
        rowCount = len(A)
        colCount = len(A[0])

        rottingGrid = {(m, n) for m in range(rowCount) for n in range(colCount) if A[m][n] == 2}
        freshGrid = {(m, n) for m in range(rowCount) for n in range(colCount) if A[m][n] == 1}

        while freshGrid:
            if not rottingGrid:
                return -1

            rottingGrid = {(x + dx, y + dy) for x, y in rottingGrid
                       for dx, dy in Solution.moves if (x + dx, y + dy) in freshGrid}
            freshGrid -= rottingGrid
            result += 1

        return result


sol = Solution()
print(sol.solve([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))  # 4
print(sol.solve([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))  # -1
