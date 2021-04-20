# Given an array of integers A of size N where N is even.
# Divide the array into two subsets such that
# 1.Length of both subset is equal.
# 2.Each element of A occurs in exactly one of these subset.
# Magic number = sum of absolute difference of corresponding elements of subset.
# Note: You can reorder the position of elements within the subset to find the value of magic number.
# For Ex:-
# subset 1 = {1, 5, 1},
# subset 2 = {1, 7, 11}
# Magic number = abs(1 - 1) + abs(5 - 7) + abs(1 - 11) = 12
# Return an array B of size 2, where
# B[0] = maximum possible value of a Magic number modulo 10^9 + 7,
# B[1] = minimum possible value of a Magic number modulo 10^9 + 7.
# 1 <= N <= 10^5
# -10^9 <= A[i] <= 10^9
# N is even
def maxMinMagic(A):
    pass


print(maxMinMagic([3, 11, -1, 5]))  # [14, 10]
print(maxMinMagic([2, 2]))  # [0, 0]
