# Given an array of numbers A , in which exactly two elements appear only once
# and all the other elements appear exactly twice. Find the two elements that appear only once.
# Note: Output array must be sorted.
# 2 <= |A| <= 100000
# 1 <= A[i] <= 10^9
from functools import reduce


def singleNumber3(A):
    a = 0
    b = 0
    arrayXor = reduce(lambda x, y: x ^ y, A)
    rightMostOne = arrayXor & -arrayXor
    for item in A:
        if rightMostOne & item:
            a ^= item
        else:
            b ^= item

    result = [a, b]
    return sorted(result)


print(singleNumber3([1, 2, 3, 1, 2, 4]))  # [3, 4]
print(singleNumber3([1, 2]))  # [1, 2]
