# Given a 2-D board A of size N x M containing 'X' and 'O', capture all regions surrounded by 'X'.
# A region is captured by flipping all 'O's into 'X's in that surrounded region.
# 1 <= N, M <= 1000
# First and only argument is a N x M character matrix A.
# Make changes to the the input only as matrix is passed by reference.
class Solution:
    moves = ((0, 1), (1, 0), (0, -1), (-1, 0))

    def util(self, A, i, j):
        if A[i][j] != 'O':
            return

        A[i][j] = '1'

        for move in Solution.moves:
            tx, ty = move
            if 0 <= i + tx < len(A) and 0 <= j + ty < len(A[i + tx]):
                self.util(A, i + tx, j + ty)

    def flipCells(self, A):
        for i in range(len(A)):
            for j in range(len(A[i])):
                if A[i][j] == 'O':
                    A[i][j] = 'X'
                elif A[i][j] == '1':
                    A[i][j] = 'O'

    # @param A : list of list of chars
    def solve(self, A):
        if not A:
            return

        for i in range(len(A)):
            if A[i][0] == 'O':
                self.util(A, i, 0)
            if A[i][len(A[i]) - 1] == 'O':
                self.util(A, i, len(A[i]) - 1)

        for j in range(len(A[0])):
            if A[0][j] == 'O':
                self.util(A, 0, j)
            if A[len(A) - 1][j] == 'O':
                self.util(A, len(A) - 1, j)

        self.flipCells(A)


sol = Solution()
B = [['X', 'X', 'X', 'X'], ['X', 'O', 'O', 'X'], ['X', 'X', 'O', 'X'], ['X', 'O', 'X', 'X']]
sol.solve(B)
print(B)
# [['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['X', 'O', 'X', 'X']]

B = [['X', 'O', 'O'], ['X', 'O', 'X'], ['O', 'O', 'O']]
sol.solve(B)
print(B)
# [['X', 'O', 'O'], ['X', 'O', 'X'], ['O', 'O', 'O']]
