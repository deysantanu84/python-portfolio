# Given two sorted integer arrays A and B, merge B and A as one sorted array and return it as an output.
# -10^10 <= A[i],B[i] <= 10^10
def merge2SortedArrays(A, B):
    N1 = len(A)
    N2 = len(B)
    C = [None] * (N1 + N2)
    p = 0
    q = 0
    r = 0

    while p < N1 and q < N2:
        if A[p] < B[q]:
            C[r] = A[p]
            r += 1
            p += 1
        else:
            C[r] = B[q]
            r += 1
            q += 1

    while p < N1:
        C[r] = A[p]
        r += 1
        p += 1

    while q < N2:
        C[r] = B[q]
        r += 1
        q += 1

    return C


print(merge2SortedArrays([1, 3, 5, 7], [2, 4, 6, 8]))  # [1, 2, 3, 4, 5, 6, 7, 8]
print(merge2SortedArrays([4, 7, 9], [2, 11, 19]))  # [2, 4, 7, 9, 11, 19]
print(merge2SortedArrays([1], [2]))  # [1, 2]
