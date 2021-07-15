import sys
sys.setrecursionlimit(2 * 10**9)
fibDict = {}


# Memory Limit Exceeded
def fibonacci(x):
    if x == 1 or x == 2:
        fibDict[x] = 1
        return 1

    if x - 2 not in fibDict.keys():
        fibDict[x - 2] = fibonacci(x - 2)

    if x - 1 not in fibDict.keys():
        fibDict[x - 1] = fibonacci(x - 1)

    if x not in fibDict.keys():
        fibDict[x] = fibDict[x - 1] + fibDict[x - 2]

    return fibDict[x]


def primeFibonacci(A, B):
    count = 0
    for i in range(A, B + 1):
        fibonacci(i)
    for i in range(A, B + 1):
        if str(fibDict[i])[-1] in ['2', '3', '5', '7']:
            count += 1

    return count


print(primeFibonacci(1, 5))  # 3
print(primeFibonacci(7, 12))  # 2
print(primeFibonacci(997, 1251))  # 119
