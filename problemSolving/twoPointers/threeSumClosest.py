# Given an array A of N integers, find three integers in A
# such that the sum is closest to a given number B. Return the sum of those three integers.
# Assume that there will only be one solution.
# -10^8 <= B <= 10^8
# 1 <= N <= 10^4
# -10^8 <= A[i] <= 10^8
import sys
INT_MAX = sys.maxsize - 1


def threeSumClosest(A, B):
    A.sort()
    N = len(A)
    result = INT_MAX
    for i in range(N - 2):
        left = i + 1
        right = N - 1
        while left < right:
            tempSum = A[i] + A[left] + A[right]
            if abs(B - tempSum) < abs(B - result):
                result = tempSum
            if tempSum > B:
                right -= 1
            else:
                left += 1
    return result


print(threeSum([-1, 2, 1, -4], 1))  # 2
print(threeSum([1, 2, 3], 6))  # 6
