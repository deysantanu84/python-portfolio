# Given an integer A, generate a square matrix filled with elements from 1 to A^2 in spiral order.
# 1 ---> 2
# |      |
# |      |
# 4 <--- 3
# [[1, 2], [4, 3]]
# 1 ---> 2 ---> 3
# |             |
# |             |
# 8 ---> 9      4
# |             |
# |             |
# 7 <--- 6 <--- 5
# [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
def spiralMatrix(A):
    matrix = []
    # Initialize AxA 0-matrix
    for i in range(A):
        col = []
        for j in range(A):
            col.append(0)
        matrix.append(col)

    top = 0
    bottom = A - 1
    left = 0
    right = A - 1
    entry = 1
    while left <= right and top <= bottom:
        for i in range(left, right + 1):
            matrix[top][i] = entry
            entry += 1
        top += 1
        for i in range(top, bottom + 1):
            matrix[i][right] = entry
            entry += 1
        right -= 1
        for i in range(right, left - 1, -1):
            matrix[bottom][i] = entry
            entry += 1
        bottom -= 1
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = entry
            entry += 1
        left += 1
    return matrix


print(spiralMatrix(1))
print(spiralMatrix(2))
print(spiralMatrix(3))
print(spiralMatrix(4))
