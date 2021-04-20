# Given an integer array A of size N.
# Find the minimum number of elements that need to be removed
# such that the GCD of the resulting array becomes 1.
# If not possible then return -1.
# 1 <= N <= 100000
# 1 <= A[i] <= 1e9
from math import gcd


def deleteElements(A):
    arrayGcd = 0
    for i in range(len(A)):
        arrayGcd = gcd(arrayGcd, A[i])

    if arrayGcd > 1:
        return -1
    else:
        return 0


print(deleteElements([7, 2, 5]))
print(deleteElements([3, 6, 12, 81, 9]))
