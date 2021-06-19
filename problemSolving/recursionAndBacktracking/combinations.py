# Given two integers A and B, return all possible combinations of B numbers out of 1 2 3 ... A .
# Make sure the combinations are sorted.
# To elaborate,
# Within every entry, elements should be sorted. [1, 4] is a valid entry while [4, 1] is not.
# Entries should be sorted within themselves.
# WARNING: DO NOT USE LIBRARY FUNCTION FOR GENERATING COMBINATIONS.
# 1 <= A, B <= 10
# Return a 2-D vector denoting all possible combinations.
def backtrack(A, B, combination, next, result):
    if B == 0:
        result.append(combination.copy())
    else:
        for i in range(next, A + 1):
            combination.append(i)
            backtrack(A, B - 1, combination, i + 1, result)
            combination.pop()


def combinations(A, B):
    result = []
    backtrack(A, B, [], 1, result)
    return result


print(combinations(4, 2))  # [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
print(combinations(3, 2))  # [[1, 2], [1, 3], [2, 3]]
