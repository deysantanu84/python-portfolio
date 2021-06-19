# Given a M x N grid A of integers, find a path from top left to bottom right
# which minimizes the sum of all numbers along its path.
# Return the minimum sum of the path.
# NOTE: You can only move either down or right at any point in time.
# 1 <= M, N <= 2000
# -1000 <= A[i][j] <= 1000
# First and only argument is a 2-D grid A.
# Return an integer denoting the minimum sum of the path.
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minPathSum(self, A):
        for i in range(len(A)):
            for j in range(len(A[0])):
                if i > 0 and j > 0:
                    A[i][j] = min(A[i][j] + A[i-1][j], A[i][j] + A[i][j-1])

                elif i > 0:
                    A[i][j] += A[i-1][j]

                elif j > 0:
                    A[i][j] += A[i][j-1]

        return A[-1][-1]


sol = Solution()
print(sol.minPathSum([[1, 3, 2], [4, 3, 1], [5, 6, 1]]))  # 8
print(sol.minPathSum([[1, -3, 2], [2, 5, 10], [5, -5, 1]]))  # -1
