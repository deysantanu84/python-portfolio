# Given a array of integers A of size N and an integer B.
# Return number of non-empty subsequences of A of size B having sum <= 1000.
# 1 <= N <= 20
# 1 <= A[i] <= 1000
# 1 <= B <= N
count = 0


def getSubsequence(A, N, i, B, currSum):
    print(i, B, currSum)
    if currSum < 0 or i > N - 1 or B < 0:
        return 0
    if currSum >= 0 and B == 0:
        return 1

    return getSubsequence(A, N, i + 1, B - 1, currSum - A[i])\
        + getSubsequence(A, N, i + 1, B, currSum)


def sixlets(A, B):
    return getSubsequence(A, len(A), 0, B, 1000)


def comb(A, N, B, ipos, op, opos, result):
    if opos == B:
        Sum = 0
        for i in range(opos):
            Sum += op[i]

        if Sum <= 1000:
            result += 1

        return

    if ipos < N:
        comb(A, N, B, ipos + 1, op, opos, result)
        op[opos] = A[ipos]
        comb(A, N, B, ipos + 1, op, opos + 1, result)


def solve(A, B):
    result = 0
    N = len(A)
    op = [0 for _ in range(N)]
    comb(A, N, B, 0, op, 0, result)
    return result


# TLE
# print(sixlets([1, 2, 8], 2))  # 3
# print(sixlets([5, 17, 1000, 11], 4))  # 0
print(solve([1, 2, 8], 2))  # 3
print(solve([5, 17, 1000, 11], 4))  # 0
