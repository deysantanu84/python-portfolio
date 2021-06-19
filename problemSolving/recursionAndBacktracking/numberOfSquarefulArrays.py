# Given an array of integers A, the array is squareful if for every pair of
# adjacent elements, their sum is a perfect square.
# Find and return the number of permutations of A that are squareful.
# Two permutations A1 and A2 differ if and only if there is some index i such that A1[i] != A2[i].
# 1 <= length of the array <= 12
# 1 <= A[i] <= 10^9
from math import sqrt, floor


def backtrack(A, index, visited, result):
    if index > 1:
        val = A[index - 2] + A[index - 1]
        isSquare = sqrt(val) == floor(sqrt(val))
        if not isSquare:
            return

    if index == len(A):
        result.append(A)
        return

    for i in range(index, len(A)):
        A[index], A[i] = A[i], A[index]

        search = (index, A[index], tuple(A[:index]))
        if search not in visited:
            visited.add(search)
            backtrack(A, index + 1, visited, result)

        A[index], A[i] = A[i], A[index]


def numberSquarefulPerms(A):
    if len(A) < 2:
        return 0
    
    result = []
    visited = set()

    backtrack(A, 0, visited, result)

    return len(result)


print(numberSquarefulPerms([2, 2, 2]))  # 1
print(numberSquarefulPerms([1, 17, 8]))  # 2
print(numberSquarefulPerms([41]))  # 0
