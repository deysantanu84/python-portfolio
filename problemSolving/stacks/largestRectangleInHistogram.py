# Given an array of integers A .
# A represents a histogram i.e A[i] denotes height of the ith histogram's bar. Width of each bar is 1.
# Find the area of the largest rectangle formed by the histogram.
# 1 <= |A| <= 100000
# 1 <= A[i] <= 1000000000
def largestRectangleInHistogram(A):
    result = 0
    A.append(0)
    stack = [-1]

    for index in range(len(A)):

        while A[index] < A[stack[-1]]:
            height = A[stack.pop()]
            width = index - stack[-1] - 1
            result = max(result, height * width)

        stack.append(index)

    A.pop()

    return result


print(largestRectangleInHistogram([2, 1, 5, 6, 2, 3]))  # 10
print(largestRectangleInHistogram([2]))  # 2
