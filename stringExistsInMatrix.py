# Given a M x N matrix, and a string, check if the entire string exists within the matrix.
# You are allowed to check for the continuation of the string in each of the 8 directions
# north, south, east, west, north-east, north-west, south-east, south-west
def getNeighbours(rowCount, columnCount, rowIndex, columnIndex):
    neighbours = []

    if 0 <= rowIndex - 1 < rowCount:
        # north
        neighbours.append([rowIndex - 1, columnIndex])

        # north-east
        neighbours.append([rowIndex - 1, columnIndex + 1])

    if 0 <= columnIndex - 1 < columnCount:
        # west
        neighbours.append([rowIndex, columnIndex - 1])

        # south-west
        neighbours.append([rowIndex + 1, columnIndex - 1])

    if 0 <= rowIndex - 1 < rowCount and 0 <= columnIndex - 1 < columnCount:
        # north-west
        neighbours.append([rowIndex - 1, columnIndex - 1])

    # south
    neighbours.append([rowIndex + 1, columnIndex])

    # east
    neighbours.append([rowIndex, columnIndex + 1])

    # south-east
    neighbours.append([rowIndex + 1, columnIndex + 1])

    return neighbours


def findContinuationAt(matrix, rowCount, columnCount, string, startAt, rowIndex, columnIndex):
    # If all string characters matched
    if startAt == len(string):
        return True

    # If row or column index lies outside the matrix, return False
    if rowIndex < 0 or rowIndex >= rowCount or columnIndex < 0 or columnIndex >= columnCount:
        return False

    # If entry does not match, return False
    if matrix[rowIndex][columnIndex] != string[startAt]:
        return False

    # Mark visited
    temp = matrix[rowIndex][columnIndex]
    matrix[rowIndex][columnIndex] = 'visited'

    # Fetch all neighbours
    neighbours = getNeighbours(rowCount, columnCount, rowIndex, columnIndex)

    # Check if pattern matches for each neighbour recursively
    for neighbour in neighbours:
        # If match found, mark unvisited and return True
        if findContinuationAt(matrix, rowCount, columnCount, string, startAt + 1, neighbour[0], neighbour[1]):
            matrix[rowIndex][columnIndex] = temp
            return True


def stringExistsInMatrix(matrix, rowCount, columnCount, string):
    # String to be searched is longer than total entries in matrix
    if len(string) > rowCount * columnCount:
        return False

    # Check each entry in matrix
    for i in range(rowCount):
        for j in range(columnCount):
            if findContinuationAt(matrix, rowCount, columnCount, string, 0, i, j):
                return True

    # Pattern not found
    return False


rows = 5
cols = 5
A = [['a', 'b', 'c', 'd', 'e'],
     ['a', 's', 't', 'd', 'e'],
     ['a', 'n', 'c', 'd', 'e'],
     ['a', 't', 'a', 'u', 'e'],
     ['n', 't', 'n', 'd', 'e']]
print(stringExistsInMatrix(A, rows, cols, 'santanu'))  # True

A = [['a', 'b', 'c', 'd', 'e'],
     ['a', 's', 't', 'd', 'e'],
     ['a', 'n', 'c', 'd', 'e'],
     ['a', 't', 'c', 'd', 'e'],
     ['n', 'u', 'c', 'd', 'e']]
print(stringExistsInMatrix(A, rows, cols, 'santanu'))  # True

A = [['a', 'b', 'c', 'd', 'e'],
     ['a', 's', 't', 'd', 'e'],
     ['a', 'n', 'c', 'd', 'e'],
     ['a', 't', 'c', 'd', 'e'],
     ['n', 't', 'c', 'd', 'e']]
print(stringExistsInMatrix(A, rows, cols, 'santanu'))  # False
