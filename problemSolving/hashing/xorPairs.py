# Given an 1D integer array A containing N distinct integers.
# Find the number of unique pairs of integers in the array whose XOR is equal to B.
# NOTE: Pair (a, b) and (b, a) is considered to be same and should be counted once.
def xorPairs(A, B):
    count = 0
    xorPairsDict = {}
    for i in range(len(A)):
        if B ^ A[i] in xorPairsDict.keys():
            count += 1
        elif A[i] not in xorPairsDict.keys():
            xorPairsDict[A[i]] = i + 1
    return count


print(xorPairs([5, 4, 10, 15, 7, 6], 5))  # 1
print(xorPairs([3, 6, 8, 10, 15, 50], 5))  # 2
