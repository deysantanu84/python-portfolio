# The n-queens puzzle is the problem of placing n queens on an n×n chessboard
# such that no two queens attack each other.
# Given an integer A, return all distinct solutions to the n-queens puzzle.
# Each solution contains a distinct board configuration of the n-queens' placement,
# where 'Q' and '.' both indicate a queen and an empty space respectively.
# 1 <= A <= 10
# First argument is an integer n denoting the size of chessboard
# Return an array consisting of all distinct solutions in which each element
# is a 2d char array representing a unique solution.
result = []


def isValid(board, row, col):
    for i in range(col):
        if board[row][i]:
            return False
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1
    i = row
    j = col
    while j >= 0 and i < 4:
        if board[i][j]:
            return False
        i = i + 1
        j = j - 1
    return True


def placeNQueens(A, board, col):
    if col == A:
        v = []
        for i in board:
            for j in range(len(i)):
                if i[j] == 1:
                    v.append(j+1)
        result.append(v)
        return True

    res = False
    for i in range(A):
        if isValid(board, i, col):
            board[i][col] = 1
            res = placeNQueens(A, board, col + 1) or res
            board[i][col] = 0
    return res


def NQueens(A):
    result.clear()
    board = [[0 for _ in range(A)]
			for _ in range(A)]
    placeNQueens(A, board, 0)
    result.sort()
    return result


print(NQueens(4))
