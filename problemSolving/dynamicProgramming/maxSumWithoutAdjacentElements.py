# Given a 2 x N grid of integer, A, choose numbers such that the sum of the numbers is maximum
# and no two chosen numbers are adjacent horizontally, vertically or diagonally, and return it.
# Note: You can choose more than 2 numbers.
# 1 <= N <= 20000
# 1 <= A[i] <= 2000
# The first and the only argument of input contains a 2d matrix, A.
# Return an integer, representing the maximum possible sum.
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def adjacent(self, A):
        N = len(A[0])
        temp1 = max(A[0][0], A[1][0])
        temp2 = 0

        for i in range(1, N):
            currMax = max(temp2, temp1)
            temp1 = temp2 + max(A[0][i], A[1][i])
            temp2 = currMax

        return max(temp2, temp1)


sol = Solution()
print(sol.adjacent([[1], [2]]))  # 2
print(sol.adjacent([[1, 2, 3, 4], [2, 3, 4, 5]]))  # 8
