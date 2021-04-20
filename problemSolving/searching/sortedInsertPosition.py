# Given a sorted array A of size N and a target value B,
# return the index (0-based indexing) if the target is found.
# If not, return the index where it would be if it were inserted in order.
# NOTE: You may assume no duplicates in the array. Users are expected to solve this in O(log(N)) time.
# 1 <= N <= 10^6
# First argument is an integer array A of size N.
# Second argument is an integer B.
def sortedInsertPosition(A, B):
    N = len(A)
    start = 0
    end = N - 1

    while start <= end:
        mid = start + (end - start) // 2
        if A[mid] == B:
            return mid
        elif A[mid] < B:
            start = mid + 1
        else:
            end = mid - 1

    return end + 1


print(sortedInsertPosition([1, 3, 5, 6], 2))  # 1
print(sortedInsertPosition([1], 1))  # 0
