# Given an array of integers A consisting of only 0 and 1.
# Find the maximum length of a contiguous sub-array with equal number of 0 and 1.
def contiguousArray(A):
    maxLenDict = {}

    A = [-1 if not A[i] else 1 for i in range(len(A))]

    tempSum = 0
    result = 0
    for index in range(len(A)):
        tempSum += A[index]
        if not tempSum:
            result = index + 1

        if tempSum in maxLenDict:
            if result < index - maxLenDict[tempSum]:
                result = index - maxLenDict[tempSum]
        else:
            maxLenDict[tempSum] = index

    # A = [0 if A[i] == -1 else 1 for i in range(len(A))]

    return result


print(contiguousArray([1, 0, 1, 0, 1]))  # 4
print(contiguousArray([1, 1, 1, 0]))  # 2
