# Given a array of integers A of size N and an integer B.
# Return number of non-empty subsequences of A of size B having sum <= 1000.
# 1 <= N <= 20
# 1 <= A[i] <= 1000
# 1 <= B <= N
count = 0


def getSubsequence(A, B, x, subsequence):
    global count
    if x == len(A):
        if len(subsequence) == B and sum(subsequence) <= 1000:
            count += 1
    else:
        getSubsequence(A, B, x + 1, subsequence)
        getSubsequence(A, B, x + 1, subsequence + [A[x]])
    return count


def sixlets(A, B):
    global count
    count = 0
    return getSubsequence(A, B, 0, [])


# TLE
print(sixlets([1, 2, 8], 2))  # 3
print(sixlets([5, 17, 1000, 11], 4))  # 0
