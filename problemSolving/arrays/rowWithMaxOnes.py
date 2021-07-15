# Given a binary sorted matrix A of size N x N. Find the row with the maximum number of 1.
# NOTE:
# If two rows have the maximum number of 1 then return the row which has a lower index.
# Rows are numbered from top to bottom and columns are numbered from left to right.
# Assume 0-based indexing.
# Assume each row to be sorted by values.
# Expected time complexity is O(rows).
def findRowWithMaxOnes(A):
    row = 0
    col = 0
    N = len(A)  # number of rows
    M = len(A[0])  # number of columns
    while col < M:
        while row < N:
            if A[row][col] == 1:
                return row
            else:
                row += 1
        row = 0
        col += 1


print(findRowWithMaxOnes([[0, 1, 1], [0, 0, 1], [0, 1, 1]]))
print(findRowWithMaxOnes([[0, 0, 0, 0], [0, 1, 1, 1]]))
