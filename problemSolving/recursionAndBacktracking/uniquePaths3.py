# Given a matrix of integers A of size N x M . There are 4 types of squares in it:
# 1. 1 represents the starting square.  There is exactly one starting square.
# 2. 2 represents the ending square.  There is exactly one ending square.
# 3. 0 represents empty squares we can walk over.
# 4. -1 represents obstacles that we cannot walk over.
# Find and return the number of 4-directional walks from the starting square to the ending square,
# that walk over every non-obstacle square exactly once.
# Note: Rows are numbered from top to bottom and columns are numbered from left to right.
# 2 <= N * M <= 20
# -1 <= A[i] <= 2
def findUniquePath(rowIndex, columnIndex, matrix, visited, result, zeroesVisited, totalZeroes):
    N = len(matrix)
    M = len(matrix[0])

    visited[rowIndex][columnIndex] = True

    if matrix[rowIndex][columnIndex] == 0:
        zeroesVisited += 1

    if matrix[rowIndex][columnIndex] == 2:
        if zeroesVisited == totalZeroes:
            result += 1

        visited[rowIndex][columnIndex] = False

        return matrix, visited, result

    if rowIndex >= 1 \
            and not visited[rowIndex - 1][columnIndex] \
            and matrix[rowIndex - 1][columnIndex] != -1:
        matrix, visited, result = findUniquePath(rowIndex - 1, columnIndex, matrix, visited,
                                                 result, zeroesVisited, totalZeroes)

    if rowIndex < N - 1 \
            and not visited[rowIndex + 1][columnIndex] \
            and matrix[rowIndex + 1][columnIndex] != -1:
        matrix, visited, result = findUniquePath(rowIndex + 1, columnIndex, matrix, visited,
                                                 result, zeroesVisited, totalZeroes)

    if columnIndex >= 1 \
            and not visited[rowIndex][columnIndex - 1] \
            and matrix[rowIndex][columnIndex - 1] != -1:
        matrix, visited, result = findUniquePath(rowIndex, columnIndex - 1, matrix, visited,
                                                 result, zeroesVisited, totalZeroes)

    if columnIndex < M - 1 \
            and not visited[rowIndex][columnIndex + 1] \
            and matrix[rowIndex][columnIndex + 1] != -1:
        matrix, visited, result = findUniquePath(rowIndex, columnIndex + 1, matrix, visited,
                                                 result, zeroesVisited, totalZeroes)

    visited[rowIndex][columnIndex] = False

    return matrix, visited, result


def uniquePaths3(A):
    zeroCount = 0
    N = len(A)
    M = len(A[0])
    result = 0

    visited = [[False for _ in range(M)] for _ in range(N)]

    x = 0
    y = 0

    for i in range(N):
        for j in range(M):
            if A[i][j] == 0:
                zeroCount += 1

            elif A[i][j] == 1:
                x = i
                y = j

    A, visited, result = findUniquePath(x, y, A, visited, result, 0, zeroCount)

    return result


print(uniquePaths3([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]))  # 2
print(uniquePaths3([[0, 1], [2, 0]]))  # 0
