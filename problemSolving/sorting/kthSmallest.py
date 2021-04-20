# Find the Bth smallest element in given array A .
# NOTE: Users should try to solve it in <= B swaps.
def kthSmallest(A, B):
    A = sorted(A)
    return A[B - 1]


print((kthSmallest([2, 1, 4, 3, 2], 3)))
print((kthSmallest([1, 2], 2)))
