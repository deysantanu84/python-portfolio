# Given an array A, find the nearest smaller element G[i] for every element A[i] in the array
# such that the element has an index smaller than i.
# More formally, G[i] for an element A[i] = an element A[j] such that
# j is maximum possible AND j < i AND [j] < A[i]
# Elements for which no smaller element exist, consider next smaller element as -1.
# 1 <= |A| <= 100000
# -10^9 <= A[i] <= 10^9
def nearestSmallerElement(A):
    N = len(A)
    stack = []
    result = []

    for i in range(N):
        while len(stack) > 0 and stack[-1] >= A[i]:
            stack.pop()

        if len(stack) == 0:
            result.append(-1)
        else:
            result.append(stack[-1])

        stack.append(A[i])

    return result


print(nearestSmallerElement([4, 5, 2, 10, 8]))  # [-1, 4, -1, 2, 2]
print(nearestSmallerElement([3, 2, 1]))  # [-1, -1, -1]
