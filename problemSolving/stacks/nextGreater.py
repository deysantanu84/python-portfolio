# Given an array A, find the next greater element G[i] for every element A[i] in the array.
# The Next greater Element for an element A[i] is the first greater element on the right side of A[i] in array, A.
# More formally:
# G[i] for an element A[i] = an element A[j] such that
#     j is minimum possible AND
#     j > i AND
#     A[j] > A[i]
# Elements for which no greater element exists, consider the next greater element as -1.
# 1 <= |A| <= 10^5
# 1 <= A[i] <= 10^7
# Return an integer array representing the next greater element for each index in A.
def nextGreater(A):
    stack = []
    result = [0 for _ in range(len(A))]

    for index in range(len(A) - 1, -1, -1):

        while len(stack) > 0 and stack[-1] <= A[index]:
            stack.pop()

        if len(stack) == 0:
            result[index] = -1
        else:
            result[index] = stack[-1]

        stack.append(A[index])

    return result


print(nextGreater([4, 5, 2, 10]))  # [5, 10, 10, -1]
print(nextGreater([3, 2, 1]))  # [-1, -1, -1]
print(nextGreater([34, 35, 27, 42, 5, 28, 39, 20, 28]))  # [35, 42, 42, -1, 28, 39, -1, 28, -1]
