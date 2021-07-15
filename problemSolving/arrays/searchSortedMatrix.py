# Given a matrix of integers A of size N x M and an integer B.
# In the given matrix every row and column is sorted in increasing order.
# Find and return the position of B in the matrix in the given form:
# If A[i][j] = B then return (i * 1009 + j)
# If B is not present return -1.
# Note 1: Rows are numbered from top to bottom and columns are numbered from left to right.
# Note 2: If there are multiple B in A then return the smallest value of i*1009 +j such that A[i][j]=B.
def searchSortedMatrix(A, B):
    N = len(A)
    M = len(A[0])
    match = -1
    for i in range(N):
        for j in range(M):
            if A[i][j] == B:
                return (i+1) * 1009 + (j+1)
    return match


print(searchSortedMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2))
