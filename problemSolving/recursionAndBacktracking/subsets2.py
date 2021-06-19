# Given a collection of integers denoted by array A of size N that might contain duplicates,
# return all possible subsets.
# NOTE:
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.
# The subsets must be sorted lexicographically.
# 0 <= N <= 16
# Return a 2-D vector denoting all the possible subsets.
def depthFirstSearch(A, index, path, result):
    result.append(path)
    for i in range(index, len(A)):
        if i > index and A[i] == A[i - 1]:
            continue
        depthFirstSearch(A, i + 1, path + [A[i]], result)


def subsets2(A):
    result = []
    A.sort()
    depthFirstSearch(A, 0, [], result)
    return result


print(subsets2([1, 2, 2]))  # [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
print(subsets2([1, 1]))  # [[], [1], [1, 1]]
