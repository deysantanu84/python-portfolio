# You are given 3 sorted arrays A, B and C.
# Find i, j, k such that : max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i])) is minimized.
# Return the minimum max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i])).
# 0 <= len(A), len(B), len(c) <= 10^6
# 0 <= A[i], B[i], C[i] <= 10^7
import sys
INT_MAX = sys.maxsize - 1


def array3Pointers(A, B, C):
    M = len(A)
    N = len(B)
    P = len(C)
    currMin = INT_MAX

    resultA = 0
    resultB = 0
    resultC = 0

    i = 0
    j = 0
    k = 0
    while i < M and j < N and k < P:
        minimum = min(A[i], min(B[j], C[k]))
        maximum = max(A[i], max(B[j], C[k]))

        if maximum - minimum < currMin:
            resultA = i
            resultB = j
            resultC = k
            currMin = maximum - minimum

        if currMin == 0:
            break

        if A[i] == minimum:
            i += 1
        elif B[j] == minimum:
            j += 1
        else:
            k += 1

    return max(abs(A[resultA] - B[resultB]), abs(B[resultB] - C[resultC]), abs(C[resultC] - A[resultA]))


print(array3Pointers([1, 4, 10], [2, 15, 20], [10, 12]))  # 5
# With 10 from A, 15 from B and 10 from C.

print(array3Pointers([3, 5, 6], [2], [3, 4]))  # 1
# With 3 from A, 2 from B and 3 from C.
