# Given an array of integers A, find and return the count of divisors of each element of the array.
# NOTE: Order of the resultant array should be same as the input array.
# 1 <= length of the array <= 100000
# 1 <= A[i] <= 10^6
from math import sqrt


def countOfDivisors2(A):
    result = [2 for _ in range(len(A))]
    for item in A:
        count = 0
        for i in range(1, int(sqrt(item)) + 1):
            if not item % i:
                if item / i == i:
                    count += 1
                else:
                    count += 2
        result.append(count)
    return result


def countOfDivisors1(A):
    divisorDict = {1: 1}
    result = []
    for i in range(2, max(A) + 1):
        divisorDict[i] = 2
    for i in range(2, max(A) + 1):
        for j in range(2*i, max(A) + 1, i):
            divisorDict[j] += 1

    for item in A:
        result.append(divisorDict[item])
    return result


# TLE
def countOfDivisors(A):
    result = A
    temp = max(A) + 2
    resDict = {}

    for i in range(temp):
        resDict[i] = i

    j = 2
    while j * j < temp:
        if resDict[j] == j:
            for k in range(j * j, temp, j):
                resDict[k] = j
        j += 1

    for i in range(len(A)):
        r = 1
        x = A[i]
        while x > 1:
            p = resDict[x]
            c = 0
            while x % p == 0:
                c += 1
                x /= p

            r *= c + 1
        result[i] = r

    return result


print(countOfDivisors([2, 3, 4, 5]))  # [2, 2, 3, 2]
print(countOfDivisors([8, 9, 10]))  # [4, 3, 4]
print(countOfDivisors([3, 52, 66, 64, 14, 51, 6, 39, 5, 26, 80, 88, 60, 73, 67, 16, 1, 81, 62, 42, 83, 31, 40, 4, 32, 31, 44, 3, 20, 94, 93, 57, 2, 18, 32, 59, 91, 30, 45]))
# [2 6 8 7 4 4 4 4 2 4 10 8 12 2 2 5 1 5 4 8 2 2 8 3 6 2 6 2 6 4 4 4 2 6 6 2 4 8 6]
