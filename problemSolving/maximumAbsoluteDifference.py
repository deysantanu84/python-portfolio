# You are given an array of N integers, A1, A2, .... AN.
# Return the maximum value of f(i, j) for all 1 ≤ i, j ≤ N.
# f(i, j) is defined as |A[i] - A[j]| + |i - j|, where |x| denotes absolute value of x.
import sys
INT_MAX = sys.maxsize - 1
INT_MIN = - sys.maxsize


def maxAbsDiff(A):
    N = len(A)
    sumArray = []
    diffArray = []
    for i in range(N):
        sumArray.append(A[i] + i)
        diffArray.append(A[i] - i)

    sumArrayMax = INT_MIN
    sumArrayMin = INT_MAX
    for i in range(N):
        if sumArray[i] > sumArrayMax:
            sumArrayMax = sumArray[i]
        if sumArray[i] < sumArrayMin:
            sumArrayMin = sumArray[i]

    diffArrayMax = INT_MIN
    diffArrayMin = INT_MAX
    for i in range(N):
        if diffArray[i] > diffArrayMax:
            diffArrayMax = diffArray[i]
        if diffArray[i] < diffArrayMin:
            diffArrayMin = diffArray[i]

    return max(sumArrayMax - sumArrayMin, diffArrayMax - diffArrayMin)


print(maxAbsDiff([1, 3, -1]))  # 5
print(maxAbsDiff([2]))  # 0
