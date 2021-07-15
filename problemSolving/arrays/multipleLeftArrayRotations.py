# Given an array of integers A and multiple values in B which represents
# the indices of the array A around which left rotation of the array A needs to be performed.
# Find the rotated array for each value and return the result in the from of a matrix
# where i'th row represents the rotated array for the i'th value in B.
# The first argument given is the integer array A.
# The second argument given is the integer array B.
# Return the resultant matrix.
def solve(A, B):
    result = []
    N = len(A)
    for i in B:
        result.append(A[(i % N):] + A[:(i % N)])
    return result


print(solve([1, 2, 3, 4, 5], [2, 3]))
print(solve([5, 17, 100, 11], [1]))
