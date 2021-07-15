# https://www.geeksforgeeks.org/return-an-array-of-anti-diagonals-of-given-nn-square-matrix/
# Give a N*N square matrix, return an array of its anti-diagonals. Look at the example for more details
# Input:
# 1 2 3
# 4 5 6
# 7 8 9
# Return the following :
# [
#   [1],
#   [2, 4],
#   [3, 5, 7],
#   [6, 8],
#   [9]
# ]
def antiDiagonals(A):
    columns = len(A)
    rows = 2 * len(A) - 1
    resultArray = []
    for row in range(rows):
        resultArray.append([])
    for m in range(columns):
        for n in range(columns):
            resultArray[m+n].append(A[m][n])
    return resultArray


print(antiDiagonals([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(antiDiagonals([[1, 2], [3, 4]]))
