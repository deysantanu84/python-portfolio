# Given a matrix of integers A of size N x N, where A[i][j] represents the weight of directed edge
# from i to j (i ---> j).
# If i == j, A[i][j] = 0, and if there is no directed edge from vertex i to vertex j, A[i][j] = -1.
# Return a matrix B of size N x N where B[i][j] = shortest path from vertex i to vertex j.
# If there is no possible path from vertex i to vertex j , B[i][j] = -1
# Note: Rows are numbered from top to bottom and columns are numbered from left to right.
# 1 <= N <= 200
# -1 <= A[i][j] <= 1000000
# The first and only argument given is the integer matrix A.
# Return a matrix B of size N x N where B[i][j] = shortest path from vertex i to vertex j
# If there is no possible path from vertex i to vertex j, B[i][j] = -1.
import sys
INT_MAX = sys.maxsize


class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        N = len(A)
        for i in range(N):
            for j in range(N):
                if A[i][j] == -1:
                    A[i][j] = INT_MAX

        for k in range(N):
            for i in range(N):
                for j in range(N):
                    if A[i][k] + A[k][j] < A[i][j]:
                        A[i][j] = A[i][k] + A[k][j]

        for i in range(N):
            for j in range(N):
                if A[i][j] == INT_MAX:
                    A[i][j] = -1

        return A


sol = Solution()
print(sol.solve([[0, 50, 39], [-1, 0, 1], [-1, 10, 0]]))  # [[0, 49, 39], [-1, 0, -1], [-1, 10, 0]]
print(sol.solve([[0, 5, -1, 10], [-1, 0, 3, -1], [-1, -1, 0, 1], [-1, -1, -1, 0]]))
# [[0, 5, 8, 9], [-1, 0, 3, 4], [-1, -1, 0, 1], [-1, -1, -1, 0]]
