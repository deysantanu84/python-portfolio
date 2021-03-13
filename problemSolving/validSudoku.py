# Determine if a Sudoku is valid, according to: http://sudoku.com.au/TheRules.aspx
# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
# ["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"]
# Return 0 / 1 ( 0 for false, 1 for true ) for this problem
def notSeenInRow(P, Q):
    alreadySeen = set()
    for i in range(0, 9):
        if P[Q][i] in alreadySeen:
            return False
        if P[Q][i] != '.':
            alreadySeen.add(P[Q][i])
    return True


def notSeenInColumn(P, Q):
    alreadySeen = set()
    for i in range(0, 9):
        if P[i][Q] in alreadySeen:
            return False
        if P[i][Q] != '.':
            alreadySeen.add(P[i][Q])
    return True


def notSeenInSubBox(P, Q, R):
    alreadySeen = set()
    for row in range(0, 3):
        for column in range(0, 3):
            entry = P[row + Q][column + R]
            if entry in alreadySeen:
                return False
            if entry != '.':
                alreadySeen.add(entry)
    return True


def isValidSudoku(A):
    for row in range(len(A)):
        for column in range(len(A)):
            if not (notSeenInRow(A, row)
                    and notSeenInColumn(A, column)
                    and notSeenInSubBox(A, row - row % 3, column - column % 3)):
                return 0
    return 1


print(isValidSudoku(["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"]))
