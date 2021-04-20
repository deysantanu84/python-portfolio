# Given a sorted array of integers A of size N and an integer B.
# array A is rotated at some pivot unknown to you beforehand.
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2 ).
# You are given a target value B to search. If found in the array, return its index, otherwise return -1.
# You may assume no duplicate exists in the array.
# NOTE: Users are expected to solve this in O(log(N)) time.
# 1 <= N <= 1000000
# 1 <= A[i] <= 10^9
# all elements in A are distinct.
# The first argument given is the integer array A.
# The second argument given is the integer B.
# Return index of B in array A, otherwise return -1
def searchRotatedArray(A, start, end, B):
    if start > end:
        return -1

    mid = start + (end - start) // 2
    if A[mid] == B:
        return mid

    if A[start] <= A[mid]:
        if A[start] <= B <= A[mid]:
            return searchRotatedArray(A, start, mid - 1, B)
        return searchRotatedArray(A, mid + 1, end, B)

    if A[mid] <= B <= A[end]:
        return searchRotatedArray(A, mid + 1, end, B)
    return searchRotatedArray(A, start, mid - 1, B)


def solve(A, B):
    return searchRotatedArray(A, 0, len(A) - 1, B)


print(solve([4, 5, 6, 7, 8, 9, 1, 2, 3], 6))  # 2
print(solve([4, 5, 6, 7, 0, 1, 2, 3], 4))  # 0
print(solve([1], 1))  # 0
