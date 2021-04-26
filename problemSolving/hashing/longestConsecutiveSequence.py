# Given an unsorted integer array A of size N.
# Find the length of the longest set of consecutive elements from the array A.
def longestConsecutiveSequence(A):
    result = 0
    sequenceSet = set()
    for item in A:
        sequenceSet.add(item)
    for index in range(len(A)):
        if A[index] - 1 not in sequenceSet:
            j = A[index]
            while j in sequenceSet:
                j += 1
            result = max(result, j - A[index])
    return result


print(longestConsecutiveSequence([100, 4, 200, 1, 3, 2]))  # 4
print(longestConsecutiveSequence([2, 1]))  # 2
