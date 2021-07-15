# Find the contiguous sub-array within an array, A of length N which has the largest sum.
# Return an integer representing the maximum possible sum of the contiguous sub-array.
def maxSumContiguousSubarray(A):
    N = len(A)
    maxSum = A[0]
    tempMax = A[0]
    for i in range(1, N):
        tempMax = max(A[i], tempMax + A[i])
        maxSum = max(maxSum, tempMax)
    return maxSum


print(maxSumContiguousSubarray([1, 2, 3, 4, -10]))  # 10
print(maxSumContiguousSubarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
print(maxSumContiguousSubarray([-2, -3, 4, -1, -2, 1, 5, -3]))  # 7
