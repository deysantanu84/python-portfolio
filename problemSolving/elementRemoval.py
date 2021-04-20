# Given an integer array A of size N. In one operation,
# you can remove any element from the array,
# and the cost of this operation is the sum of all elements in the array present before this operation.
# Find the minimum cost to remove all elements from the array
def elementRemoval(A):
    cost = 0
    S = sum(A)
    A = sorted(A, reverse=True)
    while len(A):
        cost += S
        S -= A[0]
        A.remove(A[0])
    return cost


print(elementRemoval([2, 1]))  # 4
print(elementRemoval([5]))  # 5
