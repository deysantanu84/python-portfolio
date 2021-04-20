from math import gcd


def solve(A):
    count = 0
    maxList = []
    N = len(A)
    arraySum = sum(A)
    for i in range(len(A)):
        maxList.append(arraySum - A[i])
    maxSum = max(maxList)
    for entry in maxList:
        if entry == maxSum:
            count += 1
    maxGcd = gcd(count, N)
    return [count//maxGcd, N//maxGcd]


print(solve([2, 3, 2, 3]))  # [1, 2]
print(solve([3, 3, 3, 3]))  # [1, 1]
