# Given a sorted array of integers (not necessarily distinct) A and an integer B,
# find and return how many pair of integers ( A[i], A[j] ) such that i != j have sum equal to B.
# Since the number of such pairs can be very large, return number of such pairs modulo (10^9 + 7).
# 1 <= |A| <= 100000
# 1 <= A[i] <= 10^9
# 1 <= B <= 10^9
def pairsWithGivenSum2(A, B):
    frequencyDict = {}
    N = len(A)
    for i in range(N):
        if A[i] in frequencyDict.keys():
            frequencyDict[A[i]] += 1
        else:
            frequencyDict[A[i]] = 1

    pairCount = 0

    for i in range(N):
        if B - A[i] in frequencyDict.keys():
            pairCount += (frequencyDict[B - A[i]]) % (10**9 + 7)
            if B - A[i] == A[i]:
                pairCount -= 1

    return (pairCount // 2) % (10**9 + 7)


print(pairsWithGivenSum2([1, 5, 7, -1, 5], 6))  # 3
print(pairsWithGivenSum2([1, 1, 1], 2))  # 3
print(pairsWithGivenSum2([1, 1], 2))  # 1
print(pairsWithGivenSum2([2, 3, 5, 6, 10], 6))  # 0
