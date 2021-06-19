# Given an array A of non-negative integers of size N.
# Find the minimum sub-array Al, Al+1 ,..., Ar such that if we sort (in ascending order)
# that sub-array, then the whole array should get sorted. If A is already sorted, output -1.
# 1 <= N <= 1000000
# 1 <= A[i] <= 1000000
# Return an array of length 2 where First element denotes the starting index(0-based)
# and second element denotes the ending index(0-based) of the sub-array.
# If the array is already sorted, return an array containing only one element i.e. -1.
def maxUnsortedSubarray(A):
    if len(A) <= 1:
        return [-1]

    N = len(A)
    start = 0
    end = N - 1

    for i in range(N - 1):
        if A[i] > A[i + 1]:
            start = i
            break

    while end > 0:
        if A[end] < A[end - 1]:
            break
        end -= 1

    subArrayMax = A[start]
    subArrayMin = A[start]

    for i in range(start + 1, end + 1):
        if A[i] > subArrayMax:
            subArrayMax = A[i]
        if A[i] < subArrayMin:
            subArrayMin = A[i]

    for i in range(start):
        if A[i] > subArrayMin:
            start = i
            break

    i = N - 1
    while i >= end + 1:
        if A[i] < subArrayMax:
            end = i
            break
        i -= 1

    if start == end:
        return [-1]

    return [start, end]


print(maxUnsortedSubarray([13, 13, 15]))  # [-1]
print(maxUnsortedSubarray([1, 1]))  # [-1]
print(maxUnsortedSubarray([1, 3, 2, 4, 5]))  # [1, 2]
print(maxUnsortedSubarray([1, 2, 3, 4, 5]))  # [-1]
print(maxUnsortedSubarray([4, 15, 4, 4, 15, 18, 20]))  # [1, 3]
print(maxUnsortedSubarray([3, 3, 4, 5, 5, 9, 11, 13, 14, 15, 15, 16, 15, 20, 16]))  # [11, 14]
print(maxUnsortedSubarray([1, 1, 10, 10, 15, 10, 15, 10, 10, 15, 10, 15]))  # [4, 10]
print(maxUnsortedSubarray([1, 1, 2, 3, 3, 4, 8, 9, 11, 9, 11, 12, 12, 11, 9, 14, 19, 20, 20]))  # [8, 14]
print(maxUnsortedSubarray([16, 6, 18, 17, 13, 6, 18, 16, 6, 15, 15, 18, 16, 13, 16, 16, 6, 18, 15, 15]))  # [0, 19]
