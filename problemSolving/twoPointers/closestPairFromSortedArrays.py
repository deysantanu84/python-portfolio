# Given two sorted arrays of distinct integers, A and B, and an integer C,
# find and return the pair whose sum is closest to C and the pair has one element from each array.
# More formally, find A[i] and B[j] such that abs((A[i] + B[j]) - C) has minimum value.
# If there are multiple solutions find the one with minimum i and
# even if there are multiple values of j for the same i then return the one with minimum j.
# Return an array with two elements {A[i], B[j]}.
# 1 <= length of both the arrays <= 100000
# 1 <= A[i], B[i] <= 10^9
# 1 <= C <= 10^9
import sys
INT_MAX = sys.maxsize - 1


def closestPairFromSortedArrays(A, B, C):
    M = len(A)
    N = len(B)
    distance = INT_MAX
    left = 0
    right = N - 1
    resultA = -1
    resultB = -1
    while left < M and right >= 0:
        if abs(A[left] + B[right] - C) < distance:
            resultA = left
            resultB = right
            distance = abs(A[left] + B[right] - C)
        elif abs(A[left] + B[right] - C) == distance:
            if left < resultA:
                resultA = left
                resultB = right
                distance = abs(A[left] + B[right] - C)
            elif left == resultA:
                if right < resultB:
                    resultA = left
                    resultB = right
                    distance = abs(A[left] + B[right] - C)

        if A[left] + B[right] > C:
            right -= 1
        else:
            left += 1

    return [A[resultA], B[resultB]]


print(closestPairFromSortedArrays([1, 4, 5, 7], [10, 20, 30, 40], 38))  # [7, 30]
print(closestPairFromSortedArrays([1, 2, 3, 4, 5], [2, 4, 6, 8], 9))  # [1, 8]
print(closestPairFromSortedArrays([5, 10, 20], [1, 2, 30], 13))  # [10, 2]
print(closestPairFromSortedArrays([1], [2, 4], 4))  # [1, 2]
