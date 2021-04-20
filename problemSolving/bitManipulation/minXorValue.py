# Given an integer array A of N integers, find the pair of integers in the array
# which have minimum XOR value. Report the minimum XOR value.
# 2 <= length of the array <= 100000
# 0 <= A[i] <= 10^9
import sys
INT_MAX = sys.maxsize - 1


def minXorValue(A):
    result = INT_MAX
    A.sort()
    for i in range(len(A) - 1):
        result = min(result, A[i] ^ A[i + 1])
    return result


print(minXorValue([0, 2, 5, 7]))  # 2
print(minXorValue([0, 4, 7, 9]))  # 3
