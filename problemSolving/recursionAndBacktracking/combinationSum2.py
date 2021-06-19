# Given an array of size N of candidate numbers A and a target number B.
# Return all unique combinations in A where the candidate numbers sums to B.
# Each number in A may only be used once in the combination.
# Note:
# All numbers (including target) will be positive integers.
# Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
# The solution set must not contain duplicate combinations.
# Warning:
# DO NOT USE LIBRARY FUNCTION FOR GENERATING COMBINATIONS.
# Example : itertools.combinations in python.
# If you do, we will disqualify your submission and give you penalty points.
# 1 <= N <= 20
def depthFirstSearch(A, B, index, path, currSum, result):
    if currSum > B:
        return

    if currSum == B:
        result.append(path)
        return

    for i in range(index, len(A)):
        if i > index and A[i] == A[i - 1]:
            continue

        depthFirstSearch(A, B, i + 1, path + [A[i]], currSum + A[i], result)


def combinationSum2(A, B):
    result = []
    A.sort()

    depthFirstSearch(A, B, 0, [], 0, result)
    return result


print(combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))  # [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
print(combinationSum2([2, 1, 3], 3))  # [[1, 2], [3]]
print(combinationSum2([2, 5, 2, 1, 2], 5))  # [[1, 2, 2], [5]]
