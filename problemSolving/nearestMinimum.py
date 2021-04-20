import sys
INT_MAX = sys.maxsize - 1


def solve(A):
    N = len(A)
    currMinEntry = INT_MAX
    currMinDistance = INT_MAX
    indexDict = {}
    for i in range(N):
        if A[i] < currMinEntry:
            currMinEntry = A[i]
            currMinDistance = INT_MAX
        if A[i] == currMinEntry and currMinEntry in indexDict.keys():
            if i - indexDict[currMinEntry] < currMinDistance:
                currMinDistance = i - indexDict[currMinEntry]
        indexDict[A[i]] = i

    return currMinDistance


# print(solve([0, 1, 0]))  # 2
# print(solve([2, 1, 1, 2, 3, 4]))  # 1
print(solve([10, 10, 1, 20, 20, 1]))  # 3
