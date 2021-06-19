# Given a triangle, find the minimum path sum from top to bottom.
# Each step you may move to adjacent numbers on the row below.
# Adjacent numbers for jth number of row i is jth and (j+1)th numbers of row i+1
# |A| <= 1000
# A[i] <= 1000
# First and only argument is the vector of vector A defining the given triangle
# Return the minimum sum
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minimumTotal(self, A):
        for row in range(1, len(A)):
            A[row][0] += A[row - 1][0]
            A[row][-1] += A[row - 1][-1]

            for col in range(1, row):
                A[row][col] += min(A[row - 1][col], A[row - 1][col - 1])

        return min(A[-1])


sol = Solution()
print(sol.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))  # 11
print(sol.minimumTotal([[1]]))  # 1
