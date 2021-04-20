# Given an integer array A of size N.
# You have to delete one element such that the GCD(Greatest common divisor) of the remaining array is maximum.
# Find the maximum value of GCD.
# 2 <= N <= 10^5
# 1 <= A[i] <= 10^9
from math import gcd


# Idea is to find the GCD value of all the sub-sequences of length (N – 1)
# and removing the element which is not present in the sub-sequence with that GCD.
# The maximum GCD found would be the answer.
# To find the GCD of the sub-sequences optimally,
# maintain a prefixGCD[] and a suffixGCD[] array using single state dynamic programming.
# The maximum value of GCD(prefixGCD[i – 1], suffixGCD[i + 1]) is the required answer.
def deleteOne(A):
    N = len(A)
    prefixGCD = [0 for _ in range(N + 2)]
    suffixGCD = [0 for _ in range(N + 2)]

    prefixGCD[1] = A[0]
    for i in range(2, N + 1):
        prefixGCD[i] = gcd(prefixGCD[i - 1], A[i - 1])

    suffixGCD[N] = A[N - 1]
    for i in range(N - 1, 0, -1):
        suffixGCD[i] = gcd(suffixGCD[i + 1], A[i - 1])

    result = max(suffixGCD[2], prefixGCD[N - 1])

    for i in range(2, N):
        result = max(result, gcd(prefixGCD[i - 1], suffixGCD[i + 1]))

    return result


print(deleteOne([12, 15, 18]))  # 6
# If you delete 12, gcd will be 3.
# If you delete 15, gcd will be 6.
# If you delete 18, gcd will 3.
# Maximum value of gcd is 6.

print(deleteOne([5, 15, 30]))  # 15
# If you delete 5, gcd will be 15.
# If you delete 15, gcd will be 5.
# If you delete 30, gcd will be 5.
