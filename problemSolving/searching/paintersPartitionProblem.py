# Given 2 integers A and B and an array of integers C of size N.
# Element C[i] represents length of ith board.
# You have to paint all N boards [C0, C1, C2, C3 … CN-1].
# There are A painters available and each of them takes B units of time to paint 1 unit of board.
# Calculate and return minimum time required to paint all boards
# under the constraints that any painter will only paint contiguous sections of board.
# NOTE:
# 1. 2 painters cannot share a board to paint. That is to say,
# a board cannot be painted partially by one painter, and partially by another.
# 2. A painter will only paint contiguous boards.
# Which means a configuration where painter 1 paints board 1 and 3 but not 2 is invalid.
# Return the ans % 10000003.
# 1 <= A <= 1000
# 1 <= B <= 10^6
# 1 <= N <= 10^5
# 1 <= C[i] <= 10^6
def isValid(A, C, x):
    N = len(C)
    temp = x
    index = 0
    count = 1
    while index < N:
        if count > A:
            return False
        if C[index] > temp:
            count += 1
            temp = x
        else:
            temp -= C[index]
            index += 1
    return True


def paintersPartition(A, B, C):
    N = len(C)
    totalTime = 0
    for i in range(N):
        totalTime = (totalTime + C[i]) % 10000003
    start = 0
    end = totalTime * B
    result = end % 10000003
    while start <= end:
        mid = start + (end - start) // 2
        if isValid(A, C, mid/B):
            result = mid % 10000003
            end = mid - 1
        else:
            start = mid + 1
    return result % 10000003


print(paintersPartition(2, 5, [1, 10]))  # 50
print(paintersPartition(10, 1, [1, 8, 11, 3]))  # 11
