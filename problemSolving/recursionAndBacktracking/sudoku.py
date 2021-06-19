# Write a program to solve a Sudoku puzzle by filling the empty cells.
# Empty cells are indicated by the character '.'
# You may assume that there will be only one unique solution.
class Solution:
    def solveSudoku(self, A):
        n = len(A)
        rows = [set() for _ in range(n)]
        cols = [set() for _ in range(n)]
        grids = [set() for _ in range(n)]

        def addValueToBoard(row, col, val):
            rows[row].add(val)
            cols[col].add(val)
            grids[(row // 3) * 3 + (col // 3)].add(val)
            A[row][col] = str(val)

        def removeValueFromBoard(row, col, val):
            rows[row].remove(val)
            cols[col].remove(val)
            grids[(row // 3) * 3 + (col // 3)].remove(val)
            A[row][col] = "."

        def fillBoard(row, col, board):

            if row < 0 or col < 0 or row >= n or col >= n:
                return

            while not board[row][col] == '.':
                col += 1
                if col == 9:
                    col, row = 0, row + 1
                if row == 9:
                    return True

            for val in range(1, n + 1):
                if val in rows[row] or val in cols[col] or val in grids[(row // 3) * 3 + (col // 3)]:
                    continue

                addValueToBoard(row, col, val)

                if fillBoard(row, col, board):
                    return board

                removeValueFromBoard(row, col, val)

        for i in range(n):
            for j in range(n):
                if not A[i][j] == ".":
                    addValueToBoard(i, j, int(A[i][j]))

        return fillBoard(0, 0, A)


obj = Solution()
print(obj.solveSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                 [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                 ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                 [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                 [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
# [['5', '3', '4', '6', '7', '8', '9', '1', '2'],
# ['6', '7', '2', '1', '9', '5', '3', '4', '8'],
# ['1', '9', '8', '3', '4', '2', '5', '6', '7'],
# ['8', '5', '9', '7', '6', '1', '4', '2', '3'],
# ['4', '2', '6', '8', '5', '3', '7', '9', '1'],
# ['7', '1', '3', '9', '2', '4', '8', '5', '6'],
# ['9', '6', '1', '5', '3', '7', '2', '8', '4'],
# ['2', '8', '7', '4', '1', '9', '6', '3', '5'],
# ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
