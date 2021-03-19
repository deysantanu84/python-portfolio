# Given an array of positive integers A and an integer B,
# find and return first continuous sub-array which adds to B.
# If the answer does not exist return an array with a single element "-1".
# First sub-array means the sub-array for which starting index in minimum.
def subArraySum(A, B):
    startIndex = 0
    tempSum = A[0]
    for endIndex in range(1, len(A) + 1):
        while tempSum > B and startIndex < endIndex - 1:
            tempSum -= A[startIndex]
            startIndex += 1
        if tempSum == B:
            return A[startIndex:endIndex]
        elif endIndex < len(A):
            tempSum += A[endIndex]

    return [-1]


def subArraySum2(arr, sum_):
    curr_sum = arr[0]
    start = 0
    i = 1
    while i <= len(arr):
        while curr_sum > sum_ and start < i - 1:
            curr_sum = curr_sum - arr[start]
            start += 1
        if curr_sum == sum_:
            return arr[start:i]
        if i < len(arr):
            curr_sum = curr_sum + arr[i]
        i += 1
    return [-1]


print(subArraySum([1, 1000000000], 1000000000))  # 1000000000
print(subArraySum([1, 2, 3, 4, 5], 5))  # [2, 3]
print(subArraySum([5, 10, 20, 100, 105], 110))  # [-1]
