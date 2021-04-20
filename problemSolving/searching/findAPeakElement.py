# Given an array of integers A, find and return the peak element in it.
# An array element is peak if it is NOT smaller than its neighbors.
# For corner elements, we need to consider only one neighbor. We ensure that answer will be unique.
# NOTE: Users are expected to solve this in O(log(N)) time.
# 1 <= |A| <= 100000
# 1 <= A[i] <= 10^9
def findPeakElement(A, start, end, N):
    mid = start + (end - start) // 2

    if (mid == 0 or A[mid - 1] <= A[mid]) \
            and (mid == N - 1 or A[mid + 1] <= A[mid]):
        return A[mid]

    elif mid > 0 and A[mid - 1] > A[mid]:
        return findPeakElement(A, start, (mid - 1), N)

    else:
        return findPeakElement(A, (mid + 1), end, N)


def peakElement(A):
    return findPeakElement(A, 0, len(A) - 1, len(A))


print(peakElement([1, 2, 3, 4, 5]))  # 5
print(peakElement([5, 17, 100, 11]))  # 100
