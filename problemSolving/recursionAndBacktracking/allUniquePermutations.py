# Given an array A of size N denoting collection of numbers that might contain duplicates,
# return all possible unique permutations.
# NOTE: No 2 entries in the permutation sequence should be the same.
# WARNING: DO NOT USE LIBRARY FUNCTION FOR GENERATING PERMUTATIONS.
# Example : next_permutations in C++ / itertools.permutations in python.
# If you do, we will disqualify your submission retroactively and give you penalty points.
# 1 <= |A| <= 9
# result = []


def permutations2(array, start, end):
    global result
    if start == end:
        print(list(array))
        result.append(array)
        # if array not in result:
        #     result.append(array)
    else:
        for i in range(start, end + 1):
            array[start], array[i] = array[i], array[start]
            permutations2(array, start + 1, end)
            array[start], array[i] = array[i], array[start]
    return result


def permutations(start, end=None):
    if end is None:
        end = []
    global result
    if len(start) == 0:
        if end not in result:
            result.append(end)
    else:
        for i in range(len(start)):
            permutations(start[:i] + start[i + 1:], end + start[i: i + 1])
    return result


def uniquePermutations(arr):
    global result
    result = []
    # return permutations2(arr, 0, len(A) - 1)
    return permutations(arr)


def backtrack(A):
    global result, temp, visitedList
    if len(temp) == len(A):
        print(temp)

    for i in range(len(A)):
        if visitedList[i]:
            continue
        if i > 0 and A[i] == A[i - 1] and visitedList[i - 1] is False:
            continue
        visitedList[i] = True
        temp.append(A[i])
        backtrack(A)
        visitedList[i] = False
        del temp[-1]


def permuteDuplicates(A):
    global result, visitedList, temp
    A.sort()
    backtrack(A)
    return result


def getDistinctPermutations(A):
    global result, temp, visitedList
    result = permuteDuplicates(A)


visitedList = [False] * 5
result, temp = [], []

getDistinctPermutations([1, 2, 2])
# getDistinctPermutations([1, 1, 2])


def generatePermutations(A, curr, index, used, N):
    if index == N:
        return curr
    for i in range(N):
        if used[A[i]]:
            continue
        curr[index] = A[i]
        used[A[i]] = 1
        generatePermutations(A, curr, index + 1, used, N)
        used[A[i]] = 0


def allUniquePermutations(A):
    used = {}
    for item in A:
        used[item] = 0
    return generatePermutations(A, [], 0, used, len(A))


print(allUniquePermutations([1, 1, 2]))


# print(uniquePermutations([1, 1, 2]))
# print(uniquePermutations([1, 2]))
# # print(uniquePermutations([1, 2, 3, 4, 5, 6, 7, 8]))
# print(uniquePermutations([1, 2, 3]))
