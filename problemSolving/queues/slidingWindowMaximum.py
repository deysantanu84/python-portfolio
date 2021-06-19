# Given an array of integers A. There is a sliding window of size B which is
# moving from the very left of the array to the very right.
# You can only see the B numbers in the window.
# Each time the sliding window moves rightwards by one position.
# You have to find the maximum for each window.
# Return an array C, where C[i] is the maximum value in the array from A[i] to A[i+B-1].
# Refer to the given example for clarity.
# NOTE: If B > length of the array, return 1 element with the max of the array.
# 1 <= |A|, B <= 10^6
def slidingWindowMaximum(A, B):
    N = len(A)
    queue = []
    C = []

    for i in range(B):
        while queue and A[i] >= A[queue[-1]]:
            queue.pop()

        queue.append(i)

    for i in range(B, N):
        C.append(A[queue[0]])

        while queue and queue[0] <= i - B:
            queue.pop(0)

        while queue and A[i] >= A[queue[-1]]:
            queue.pop()

        queue.append(i)

    C.append(A[queue[0]])

    return C


print(slidingWindowMaximum([12, 1, 78, 90, 57, 89, 56], 3))  # [78, 90, 90, 90, 89]
print(slidingWindowMaximum([1, 3, -1, -3, 5, 3, 6, 7], 3))  # [3, 3, 5, 5, 6, 7]
print(slidingWindowMaximum([1, 2, 3, 4, 2, 7, 1, 3, 6], 6))  # [7, 7, 7, 7]
