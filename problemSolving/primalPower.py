# "Primal Power" of an array is defined as the count of prime numbers present in it.
# Given an array of integers A of length N, you have to calculate its Primal Power.
from math import sqrt, ceil


def isPrime(P):
    if P <= 1:
        return False
    if P <= 3:
        return True
    for i in range(2, ceil(sqrt(P))+1):
        if not P % i:
            return False
    return True


def solve(A):
    count = 0
    for item in A:
        if isPrime(item):
            count += 1

    return count


# print(solve([-6, 10, 12]))
print(solve([-11, 7, 8, 9, 10, 11]))
# print(isPrime(9))
