# Given character matrix A of O's and X's, where O = white, X = black.
# Return the number of black shapes. A black shape consists of one or more adjacent X's
# (diagonals not included)
# 1 <= |A|,|A[0]| <= 1000
# A[i][j] = 'X' or 'O'
# The First and only argument is character matrix A.
# Return a single integer denoting number of black shapes.
class Solution:
    moves = ((0, 1), (1, 0), (0, -1), (-1, 0))

    def util(self, A, i, j, flag):
        if A[i][j] != 'X':
            return

        A[i] = A[i][:j] + str(flag) + A[i][j + 1:]

        for move in Solution.moves:
            tx, ty = move
            if 0 <= i + tx < len(A) and 0 <= j + ty < len(A[i + tx]):
                self.util(A, i + tx, j + ty, flag)

    # @param A : list of strings
    # @return an integer
    def black(self, A):
        result = 0
        for i in range(len(A)):
            for j in range(len(A[i])):
                if A[i][j] == 'X':
                    self.util(A, i, j, '1')
                    result += 1

        return result


sol = Solution()
print(sol.black(['XXX', 'XXX', 'XXX']))  # 1
print(sol.black(['XO', 'OX']))  # 2
