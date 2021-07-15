# Given numRows, generate the first numRows of Pascal's triangle.
# Pascal's triangle : To generate A[C] in row R, sum up A'[C] and A'[C-1] from previous row R - 1.
# numRows = 5
# [
#      [1],
#      [1,1],
#      [1,2,1],
#      [1,3,3,1],
#      [1,4,6,4,1]
# ]
def pascalTriangle(A):
    result = []
    for i in range(A):
        row = []
        for j in range(i+1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(result[i-1][j-1] + result[i-1][j])
        result.append(row)
    return result


print(pascalTriangle(5))
