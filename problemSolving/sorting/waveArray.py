# Given an array of integers A, sort the array into a wave like array and return it.
# In other words, arrange the elements into a sequence such that a1 >= a2 <= a3 >= a4 <= a5.....
# NOTE : If there are multiple answers possible, return the one that's lexicographically smallest.
def waveSort(A):
    A = sorted(A)
    N = len(A)
    if N % 2:
        for i in range(0, len(A) - 1, 2):
            A[i], A[i + 1] = A[i + 1], A[i]
    else:
        for i in range(0, len(A), 2):
            A[i], A[i + 1] = A[i + 1], A[i]
    return A


# print(waveSort([1, 2, 3, 4]))
# print(waveSort([1, 2]))
print(waveSort([5, 1, 3, 2, 4]))
