# Given an integer array A of size N.
# You need to sort the elements in increasing order using SelectionSort.
# Return a array containing the min value's index position before every iteration.
# NOTE:
# Consider 0 based indexing while looking for min value in each step of selection sort.
# There will be total N - 1 iterations in selection sort so the output array will contain N - 1 integers.
# Input: A = [6, 4, 3, 7, 2, 8]
# Output: [4, 2, 2, 4, 4]
# Explanation : 6 4 3 7 2 8 : Index of 1st min - 4
# After 1st Iteration : 2 4 3 7 6 8 : Index of 2nd min - 2
# After 2nd Iteration : 2 3 4 7 6 8 : Index of 3rd min - 2
# After 3rd Iteration : 2 3 4 7 6 8 : Index of 4th min - 4
# After 4th iteration : 2 3 4 6 7 8 : Index of 5th min - 4
# After 5th iteration : 2 3 4 6 7 8
def stepwiseSelectionSort(A):
    result = []
    N = len(A)
    for i in range(N - 1):
        minIndex = i
        for j in range(i + 1, N):
            if A[minIndex] > A[j]:
                minIndex = j
        A[i], A[minIndex] = A[minIndex], A[i]
        result.append(minIndex)
    return result


print(stepwiseSelectionSort([6, 4, 3, 7, 2, 8]))
