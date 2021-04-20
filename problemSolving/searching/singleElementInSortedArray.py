# Given a sorted array of integers A where every element appears twice
# except for one element which appears once, find and return this single element that appears only once.
# NOTE: Users are expected to solve this in O(log(N)) time.
# 1 <= |A| <= 100000
# 1 <= A[i] <= 10^9
def binarySearch(A, start, end):
    if start > end:
        return None

    if start == end:
        return A[start]

    mid = start + (end - start) // 2

    if mid % 2:
        if A[mid] == A[mid - 1]:
            return binarySearch(A, mid + 1, end)
        else:
            return binarySearch(A, start, mid - 1)

    else:
        if A[mid] == A[mid + 1]:
            return binarySearch(A, mid + 2, end)
        else:
            return binarySearch(A, start, mid)


def singleElement(A):
    return binarySearch(A, 0, len(A) - 1)


print(singleElement([1, 1, 7]))  # 7
print(singleElement([2, 3, 3]))  # 2
