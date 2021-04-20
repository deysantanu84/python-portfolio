# Given a matrix of integers A of size N x M and an integer B.
# Write an efficient algorithm that searches for integer B in matrix A.
# This matrix A has the following properties:
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than or equal to the last integer of the previous row.
# Return 1 if B is present in A, else return 0.
# NOTE: Rows are numbered from top to bottom and columns are numbered from left to right.
# 1 <= N, M <= 1000
# 1 <= A[i][j], B <= 10^6
# Python program for the above approach
def rowBinarySearch(A, B, row):
    start = 0
    end = len(A[0]) - 1

    while start <= end:
        mid = start + (end - start) // 2
        if A[row][mid] == B:
            return 1

        if A[row][mid] > B:
            end = mid - 1

        if A[row][mid] < B:
            start = mid + 1

    return 0


def matrixSearch(A, B):
    rowCount = len(A)
    columnCount = len(A[0])
    start = 0
    end = rowCount - 1

    while start <= end:
        mid = start + (end - start) // 2
        if A[mid][0] == B:
            return 1

        if A[mid][columnCount - 1] == B:
            return 1

        if A[mid][0] < B < A[mid][columnCount - 1]:
            return rowBinarySearch(A, B, mid)

        if B < A[mid][0]:
            end = mid - 1

        if B > A[mid][columnCount - 1]:
            start = mid + 1

    return 0


print(matrixSearch([[0, 6, 8, 9, 11], [20, 22, 28, 29, 31], [36, 38, 50, 61, 63], [64, 66, 100, 122, 128]], 31))  # 1
print(matrixSearch([[1,   3,  5,  7], [10, 11, 16, 20], [23, 30, 34, 50]], 3))  # 1
print(matrixSearch([[5, 17, 100, 111], [119, 120, 127, 131]], 3))  # 0
