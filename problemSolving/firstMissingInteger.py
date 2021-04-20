# Given an unsorted integer array A of size N. Find the first missing positive integer.
# Note: Your algorithm should run in O(n) time and use constant space.
# https://www.geeksforgeeks.org/find-the-smallest-positive-number-missing-from-an-unsorted-array/


# All positive integers
def firstMissingPositiveInteger(arr):
    N = len(arr)
    for i in range(N):
        if abs(arr[i]) - 1 < N and arr[abs(arr[i]) - 1] > 0:
            arr[abs(arr[i]) - 1] = - arr[abs(arr[i]) - 1]
    for i in range(N):
        if arr[i] > 0:
            return i + 1
    return N + 1


# Positive and Negative Integers
def firstMissingInteger(A):
    N = len(A)
    j = 0
    for i in range(N):
        if A[i] <= 0:
            A[i], A[j] = A[j], A[i]
            j += 1
    return firstMissingPositiveInteger(A[j:])


print(firstMissingInteger([0, 10, 2, -10, -20]))  # 1
# print(firstMissingInteger([1, 2, 0]))  # 3
# print(firstMissingInteger([3, 4, -1, 1]))  # 2
# print(firstMissingInteger([-8, -7, -6]))  # 1
