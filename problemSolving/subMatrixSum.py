# Given a matrix of integers A of size N x M and multiple queries Q,
# for each query find and return the submatrix sum.
# Inputs to queries are top left (b, c) and bottom right (d, e) indexes
# of submatrix whose sum is to find out.
# NOTE:
# Rows are numbered from top to bottom and columns are numbered from left to right.
# Sum may be large so return the answer mod 10^9 + 7.
# 1 <= N, M <= 1000
# -100000 <= A[i] <= 100000
# 1 <= Q <= 100000
# 1 <= B[i] <= D[i] <= N
# 1 <= C[i] <= E[i] <= M
# The first argument given is the integer matrix A.
# The second argument given is the integer array B.
# The third argument given is the integer array C.
# The fourth argument given is the integer array D.
# The fifth argument given is the integer array E.
# (B[i], C[i]) represents the top left corner of the i'th query.
# (D[i], E[i]) represents the bottom right corner of the i'th query.
def sumMatrixSum(A, B, C, D, E):
    result = []
    for i in range(len(B)):
        result.append(0)

    prefixSumMatrix = []
    for row in range(len(A)):
        rowList = []
        for j in range(len(A[row])):
            rowList.append(0)
        prefixSumMatrix.append(rowList)

    for i in range(0, len(A[0]), 1):
        prefixSumMatrix[0][i] = A[0][i]

    for i in range(1, len(A)):
        for j in range(len(A[i])):
            prefixSumMatrix[i][j] = (A[i][j] + prefixSumMatrix[i - 1][j]) % (10**9 + 7)

    for i in range(0, len(A)):
        for j in range(1, len(A[i])):
            prefixSumMatrix[i][j] = (prefixSumMatrix[i][j] + prefixSumMatrix[i][j - 1]) % (10**9 + 7)

    for i in range(len(B)):
        result[i] = prefixSumMatrix[D[i] - 1][E[i] - 1]
        if B[i] > 1:
            result[i] = (result[i] - prefixSumMatrix[B[i] - 2][E[i] - 1]) % (10**9 + 7)

        if C[i] > 1:
            result[i] = (result[i] - prefixSumMatrix[D[i] - 1][C[i] - 2]) % (10**9 + 7)

        if B[i] > 1 and C[i] > 1:
            result[i] = (result[i] + prefixSumMatrix[B[i] - 2][C[i] - 2]) % (10**9 + 7)

    return result


print(sumMatrixSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2], [1, 2], [2, 3], [2, 3]))  # [12, 28]
# For query 1: Submatrix contains elements: 1, 2, 4 and 5. So, their sum is 12.
# For query 2: Submatrix contains elements: 5, 6, 8 and 9. So, their sum is 28.

print(sumMatrixSum([[5, 17, 100, 11], [0, 0,  2,   8]], [1, 1], [1, 4], [2, 2], [2, 4]))  # [22, 19]
# For query 1: Submatrix contains elements: 5, 17, 0 and 0. So, their sum is 22.
# For query 2: Submatrix contains elements: 11 and 8. So, their sum is 19.
