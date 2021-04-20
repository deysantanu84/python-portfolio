# Given n non-negative integers A[0], A[1], ..., A[n-1] ,
# where each represents a point at coordinate (i, A[i]).
# N vertical lines are drawn such that the two endpoints of line i is at (i, A[i]) and (i, 0).
# Find two lines, which together with x-axis forms a container,
# such that the container contains the most water.
# Note: You may not slant the container.
# 0 <= N <= 10^5
# 1 <= A[i] <= 10^5
# Return single Integer denoting the maximum area you can obtain.
def containerWithMostWater(A):
    result = 0
    left = 0
    right = len(A) - 1

    while left < right:
        temp = min(A[left], A[right]) * (right - left)
        result = max(result, temp)
        if A[left] < A[right]:
            left += 1
        else:
            right -= 1

    return result


print(containerWithMostWater([1]))  # 0
print(containerWithMostWater([1, 5, 4, 3]))  # 6
print(containerWithMostWater([3, 1, 2, 4, 5]))  # 12
