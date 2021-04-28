# Given an array of integers A of size N that is a permutation of [0, 1, 2, ..., (N-1)],
# if we split the array into some number of "chunks" (partitions), and individually sort each chunk.
# After concatenating them, the result equals the sorted array.
# What is the most number of chunks we could have made?
# 1 <= N <= 100000
# 0 <= A[i] < N
def maxChunksToMakeSorted(A):
    result = 0
    currMax = A[0]

    for i in range(len(A)):
        if A[i] > currMax:
            currMax = A[i]
        if i == currMax:
            result += 1

    return result


print(maxChunksToMakeSorted([1, 2, 3, 4, 0]))  # 1
print(maxChunksToMakeSorted([2, 0, 1, 3]))  # 2
