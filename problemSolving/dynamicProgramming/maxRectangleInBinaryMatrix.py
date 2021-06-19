# Given a 2-D binary matrix A of size N x M filled with 0's and 1's,
# find the largest rectangle containing all ones and return its area.
# 1 <= N, M <= 100
# First argument is an 2-D binary array A.
# Return an integer denoting the area of largest rectangle containing all ones.
import sys
INT_MIN = -sys.maxsize


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def maximalRectangle(self, A):
        dpDict = {}
        result = 0

        for row in range(len(A)):
            for col in range(len(A[row])):
                if A[row][col] == 1:
                    if col - 1 < 0:
                        dpDict[row, col] = col
                    else:
                        if (row, col - 1) in dpDict:
                            dpDict[row, col] = dpDict[row, col - 1]
                        else:
                            dpDict[row, col] = col

        for row in range(len(A)):
            for col in range(len(A[row])):
                if A[row][col] == 1:
                    maxVal = INT_MIN

                    for i in range(row, -1, -1):
                        if (i, col) in dpDict:
                            maxVal = max(maxVal, dpDict[i, col])
                            temp = (row - i + 1) * (col - maxVal + 1)
                            result = max(result, temp)
                        else:
                            break

        return result


sol = Solution()
print(sol.maximalRectangle([[1, 1, 1], [0, 1, 1], [1, 0, 0]]))  # 4
print(sol.maximalRectangle([[0, 1, 0], [1, 1, 1]]))  # 3
