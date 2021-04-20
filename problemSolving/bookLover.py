def solve(A):
    N = len(A)
    readDict = {}
    j = 0
    for i in range(N):
        if A[i] in readDict.keys():
            readDict[A[i]] += 1
        else:
            readDict[A[i]] = 1
    print(readDict)
    for index, value in readDict.items():
        if value > 1:
            continue
    return A[j]


print(solve([4, 8, 1, 3, 1]))  # 4
# print(solve([7, 8, 4, 2, 7]))  # 8
# print(solve([1, 2, 3, 1, 2, 3]))  # 1
