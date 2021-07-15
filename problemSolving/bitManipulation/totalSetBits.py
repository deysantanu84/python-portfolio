# Given a positive integer A, the task is to count the total number of set bits
# in the binary representation of all the numbers from 1 to A.
# Return the count modulo 10^9 + 7
# https://www.geeksforgeeks.org/count-total-set-bits-in-all-numbers-from-1-to-n/
# https://www.geeksforgeeks.org/count-total-set-bits-in-all-numbers-from-1-to-n-set-2/
def getLeftmostBit(n):
    m = 0
    while n > 1:
        n = n >> 1
        m += 1
    return m


def getNextLeftmostBit(n, m):
    temp = 1 << m
    while n < temp:
        temp = temp >> 1
        m -= 1
    return m


def countSetBits(n):
    # m = getLeftmostBit(n)
    m = 0
    while n > 1:
        n = n >> 1
        m += 1
    return _countSetBits(n, m)


def _countSetBits(n, m):
    if n == 0:
        return 0

    # m = getNextLeftmostBit(n, m)
    temp = 1 << m
    while n < temp:
        temp = temp >> 1
        m -= 1

    if n == (1 << (m + 1)) - 1:
        return (m + 1) * (1 << m)

    n = n - (1 << m)
    return (n + 1) + countSetBits(n) + m * (1 << (m - 1))


def countSetBits2(A):
    i = 0
    result = 0
    while (1 << i) <= A:
        k = 0
        change = 1 << i
        for j in range(0, A + 1):
            result += k
            if change == 1:
                k = not k
                change = 1 << i
            else:
                change -= 1
        i += 1

    return result % (10 ** 7)


def countTotalSetBits3(A):
    totalBits = 0
    for item in range(1, A+1):
        bits = 0
        while item:
            bits += item & 1
            item >>= 1
        totalBits += bits
        print(item, bits, totalBits)

    return totalBits % (10**9 + 7)


def countTotalSetBits(A):
    A += 1
    i = 2
    result = A // 2
    while i <= A:
        totalPairs = A // i
        result += (totalPairs // 2) * i
        if totalPairs & 1:
            result += (A % i)
        else:
            result += 0
        i <<= 1
    return result % (10**9 + 7)


print(countTotalSetBits(3))
print(countTotalSetBits(1))
