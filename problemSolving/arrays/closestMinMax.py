# Given an array A. Find the size of the smallest sub-array such that it contains
# at least one occurrence of the maximum value of the array
# and at least one occurrence of the minimum value of the array.
import sys
INT_MIN = - sys.maxsize
INT_MAX = sys.maxsize - 1


def closestMinMax(A):
    minIndex = INT_MIN
    maxIndex = INT_MIN
    arrayMin = min(A)
    arrayMax = max(A)
    result = INT_MAX
    for i in range(len(A)):
        if A[i] == arrayMin:
            minIndex = i
            result = min(result, minIndex - maxIndex + 1)
        if A[i] == arrayMax:
            maxIndex = i
            result = min(result, maxIndex - minIndex + 1)
    return result


print(closestMinMax([1, 3]))
print(closestMinMax([2]))
print(closestMinMax([5, 6, 3, 2, 4, 1, 9, 8, 9, 6, 10]))
