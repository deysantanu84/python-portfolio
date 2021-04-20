# Write a program to solve a Sudoku puzzle by filling the empty cells.
# Empty cells are indicated by the character '.'
# You may assume that there will be only one unique solution.
def printResult(A):
    for i in range(9):
        for j in range(9):
            print(A[i][j], end='')
        print()


def isEmptyLocation(arr, temp):
    for row in range(9):
        for col in range(9):
            if arr[row][col] == 0:
                temp[0] = row
                temp[1] = col
                return True
    return False


def checkRow(arr, row, num):
    for i in range(9):
        if arr[row][i] == num:
            return True
    return False


def checkColumn(arr, col, num):
    for i in range(9):
        if arr[i][col] == num:
            return True
    return False


def checkBox(arr, row, col, num):
    for i in range(3):
        for j in range(3):
            if arr[i + row][j + col] == num:
                return True
    return False


def isValidLocation(arr, row, col, num):
    return not checkRow(arr, row, num) \
           and not checkColumn(arr, col, num) \
           and not checkBox(arr, row - row % 3, col - col % 3, num)


def sudoku(A):
    temp = [0, 0]
    if not isEmptyLocation(A, temp):
        return True
    row = temp[0]
    col = temp[1]

    for i in range(1, 10):
        if isValidLocation(A, row, col, i):
            A[row][col] = i
            if sudoku(A):
                printResult(A)
            A[row][col] = 0
    return False


print(sudoku([[3, 0, 6, 5, 0, 8, 4, 0, 0],
            [5, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 7, 0, 0, 0, 0, 3, 1],
            [0, 0, 3, 0, 1, 0, 0, 8, 0],
            [9, 0, 0, 8, 6, 3, 0, 0, 5],
            [0, 5, 0, 0, 9, 0, 6, 0, 0],
            [1, 3, 0, 0, 0, 0, 2, 5, 0],
            [0, 0, 0, 0, 0, 0, 0, 7, 4],
            [0, 0, 5, 2, 0, 6, 3, 0, 0]]))
