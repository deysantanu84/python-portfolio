# Given an array of integers A. If i < j and A[i] > A[j] then the pair (i, j)
# is called an inversion of A. Find the total number of inversions of A modulo (10^9 + 7).
# 1 <= length of the array <= 100000
# 1 <= A[i] <= 10^9
def merge(A, temp, start, mid, end):
    count = 0
    p = start
    q = mid + 1
    r = start
    while p <= mid and q <= end:
        if A[p] <= A[q]:
            temp[r] = A[p]
            r += 1
            p += 1
        else:
            temp[r] = A[q]
            count += (mid - p + 1) % (10**9 + 7)
            r += 1
            q += 1

    while p <= mid:
        temp[r] = A[p]
        r += 1
        p += 1

    while q <= end:
        temp[r] = A[q]
        r += 1
        q += 1

    for i in range(start, end + 1):
        A[i] = temp[i]

    return count


def mergeSort(A, temp, start, end):
    count = 0

    if start < end:
        mid = start + (end - start) // 2
        count += mergeSort(A, temp, start, mid) % (10**9 + 7)
        count += mergeSort(A, temp, mid + 1, end) % (10**9 + 7)
        count += merge(A, temp, start, mid, end) % (10**9 + 7)

    return count % (10**9 + 7)


def inversionCount(A):
    N = len(A)
    temp = [0] * N
    return mergeSort(A, temp, 0, N - 1)


print(inversionCount([1, 20, 6, 4, 5]))  # 5
print(inversionCount([3, 2, 1]))  # 3
print(inversionCount([1, 2, 3]))  # 0
