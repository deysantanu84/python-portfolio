# Given a 2D Matrix A of dimensions N*N, we need to return sum of all possible submatrices.
def sumOfAllSubMatrices(A):
    N = len(A)
    result = 0
    for i in range(N):
        for j in range(N):
            topLeft = (i + 1) * (j + 1)
            bottomRight = (N - i) * (N - j)
            result += (topLeft * bottomRight * A[i][j])
    return result


print(sumOfAllSubMatrices([[1, 1], [1, 1]]))  # 16
print(sumOfAllSubMatrices([[1, 1, 1], [1, 1, 1], [1, 1, 1]]))  # 100
