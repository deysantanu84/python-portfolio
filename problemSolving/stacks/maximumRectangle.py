# Given a 2D binary matrix of integers A containing 0's and 1's of size N x M.
# Find the largest rectangle containing only 1's and return its area.
# Note: Rows are numbered from top to bottom and columns are numbered from left to right.
# 1 <= N, M <= 1000
# 0 <= A[i] <= 1
def largestArea(array):
    stack = [-1]
    array.append(0)
    result = 0

    for index in range(len(array)):

        while array[index] < array[stack[-1]]:
            height = array[stack.pop()]
            width = index - stack[-1] - 1
            result = max(result, height * width)

        stack.append(index)

    return result


def maximumRectangle(A):
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] == 1:
                A[i][j] = int(A[i][j]) + int(A[i - 1][j] if (i > 0) else 0)
            else:
                A[i][j] = 0

    result = 0

    for row in A:
        result = max(result, largestArea(row))

    return result


print(maximumRectangle([[0, 0, 1], [0, 1, 1], [1, 1, 1]]))  # 4
print(maximumRectangle([[0, 1, 0, 1], [1, 0, 1, 0]]))  # 1
