# Print a Pattern According to The Given Value of A.
#     1
#   2 1
# 3 2 1
# First and only argument is an integer denoting A.
# Return a two-dimensional array where each row in the returned array represents a row in the pattern.
def printPattern2(A):
    result = []
    for i in range(A):
        row = []
        for j in range(A):
            row.append(0)
        result.append(row)

    for i in range(A):
        columnIndex = A - 1
        for j in range(1, i+2):
            result[i][columnIndex] = j
            columnIndex -= 1
    return result


print(printPattern2(3))
print(printPattern2(4))
