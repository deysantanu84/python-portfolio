# Given an array of integers A, find and return the minimum value
# of | A [ i ] - A [ j ] | where i != j and |x| denotes the absolute value of x.
# 1 <= length of the array <= 100000
# -10^9 <= A[i] <= 10^9
def minAbsoluteDifference(A):
    A.sort()
    result = max(A) - min(A)
    for i in range(len(A) - 1):
        x = abs(A[i + 1] - A[i])
        if x < result:
            result = x

    return result


print(minAbsoluteDifference([1, 2, 3, 4, 5]))  # 1
print(minAbsoluteDifference([5, 17, 100, 11]))  # 6
