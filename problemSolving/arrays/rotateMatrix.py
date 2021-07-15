# You are given a n x n 2D matrix A representing an image.
# Rotate the image by 90 degrees (clockwise).
# You need to do this in place.
# Note: If you end up using an additional array, you will only receive partial score.
def transposeMatrix(A):
    N = len(A)  # number of rows
    M = len(A[0])  # number of columns
    for i in range(N):
        for j in range(i+1, M):
            A[i][j], A[j][i] = A[j][i], A[i][j]
    return A


def rotateMatrix90(A):
    A = transposeMatrix(A)
    rows = len(A)
    for row in range(rows):
        A[row].reverse()
    return A


print(rotateMatrix90([[1, 2], [3, 4]]))
print(rotateMatrix90([[1]]))
