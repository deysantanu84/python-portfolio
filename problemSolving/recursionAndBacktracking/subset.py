# Given a set of distinct integers, A, return all possible subsets.
# NOTE:
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.
# Also, the subsets should be sorted in ascending ( lexicographic ) order.
# The list is not necessarily sorted.
result = []
temp = []


def fetchSubsets(A, index):
    global result
    global temp
    result.append(temp[:])
    for i in range(index, len(A)):
        temp.append(A[i])
        fetchSubsets(A, i + 1)
        temp.pop(-1)


def subsets(A):
    global result
    result = []
    A.sort()
    fetchSubsets(A, 0)
    return result


print(subsets([1, 2, 3]))
print(subsets([1]))
print(subsets([15, 20, 12, 19, 4]))
