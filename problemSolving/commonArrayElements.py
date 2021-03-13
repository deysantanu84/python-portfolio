# Given two integer arrays A and B of length M and N respectively
# Find all the common elements in both the arrays
# Each element in the result should appear as many times as it appears in both arrays
# The result can be in any order
# TLE
def findCommonElements(A, B):
    commonElemList = []
    index = 0
    while A:
        if A[index] in set(B):
            commonElemList.append(A[index])
            B.remove(A[index])
        A.pop(index)

    return commonElemList


# P = [1, 2, 2, 1]
# Q = [2, 3, 1, 2]
P = [2, 1, 4, 10]
Q = [3, 6, 2, 10, 10]
print(findCommonElements(P, Q))
