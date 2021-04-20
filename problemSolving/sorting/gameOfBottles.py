# Given an array of integers A of size N which denotes N cylindrical empty bottles.
# The radius of the ith bottle is A[i].
# You can put the ith bottle into the jth bottle if the following conditions are met:
# ith bottle is not put into another bottle.
# jth bottle doesn't contain any other bottle.
# The radius of bottle i is smaller than bottle j (A[i] < A[j]).
# You can put bottles into each other any number of times.
# You want to MINIMIZE the number of visible bottles.
# A bottle is called visible if it is not put into any other bottle.
# Find and return the minimum number of visible bottles.
# 1 <= N <= 100000
# 1<= A[i] <= 100000000
def gameOfBottles(A):
    N = len(A)
    bottleDict = {}
    result = 0
    for i in range(N):
        if A[i] in bottleDict.keys():
            bottleDict[A[i]] = bottleDict[A[i]] + 1
        else:
            bottleDict[A[i]] = 1
        # bottleDict[A[i]] = bottleDict.get(A[i], 0) + 1
        result = max(result, bottleDict[A[i]])

    return result


print(gameOfBottles([1, 2, 3]))  # 1
print(gameOfBottles([1, 1]))  # 2
print(gameOfBottles([1, 1, 2, 3, 4, 5, 5, 4]))  # 2
