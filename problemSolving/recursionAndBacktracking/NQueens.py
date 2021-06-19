# The n-queens puzzle is the problem of placing n queens on an n×n chessboard
# such that no two queens attack each other.
# Given an integer A, return all distinct solutions to the n-queens puzzle.
# Each solution contains a distinct board configuration of the n-queens' placement,
# where 'Q' and '.' both indicate a queen and an empty space respectively.
# 1 <= A <= 10
# First argument is an integer n denoting the size of chessboard
# Return an array consisting of all distinct solutions in which each element
# is a 2d char array representing a unique solution.
def isValid(board, rowIndex, colIndex, memo):
    if memo['row'][rowIndex]:
        return False

    if memo['col'][colIndex]:
        return False

    if memo['diagonal'][len(board) - 1 + rowIndex - colIndex]:
        return False

    if memo['reverse'][rowIndex + colIndex]:
        return False

    return True


def placeNQueens(A, currentRow, board, memo, result):
    if currentRow == A:
        result.append(["".join(row) for row in board])
        return
    for i in range(A):
        board[currentRow][i] = 'Q'
        if isValid(board, currentRow, i, memo):
            memo['row'][currentRow] = True
            memo['col'][i] = True
            memo['diagonal'][A - 1 + currentRow - i] = True
            memo['reverse'][currentRow + i] = True

            placeNQueens(A, currentRow + 1, board, memo, result)

            memo['diagonal'][A - 1 + currentRow - i] = False
            memo['reverse'][currentRow + i] = False
            memo['col'][i] = False
            memo['row'][currentRow] = False
        board[currentRow][i] = '.'


def NQueens(A):
    memo = {
        'row': [False] * A,
        'col': [False] * A,
        'diagonal': [False] * (2 * A - 1),
        'reverse': [False] * (2 * A - 1)
    }
    board = [['.'] * A for _ in range(A)]
    result = []
    placeNQueens(A, 0, board, memo, result)
    return result


print(NQueens(4))  # [['.Q..', '...Q', 'Q...', '..Q.'], ['..Q.', 'Q...', '...Q', '.Q..']]
print(NQueens(1))  # [['Q']]
