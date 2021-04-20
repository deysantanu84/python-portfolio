# Given an array of integers A of size, N.
# Minimize the absolute difference between the maximum and minimum element of the array.
# You can perform two types of operations at most B times in total to change the values in the array.
# Multiple operations can be performed on the same element.
# Increment : A[i] -> A[i] + 1.
# Decrement : A[i] -> A[i] - 1.
# Return the minimum difference possible.
def minimumDifference(A, B):
    N = len(A)
    if (max(A) - min(A)) <= B:
        return max(A) - min(A)
    for i in range(N):
        if A[i] > (max(A) + min(A)) // 2:
            A[i] -= B
        else:
            A[i] += B
    return max(A) - min(A)


print(minimumDifference([2, 6, 3, 9, 8], 3))  # 5
# We can apply the atmost 3 operations in the following sequence.
#  Initial array => [2, 6, 3, 9, 8].
#    Decrement 9 => [2, 6, 3, 8, 8].
#    Increment 2 => [3, 6, 3, 8, 8].
#    Increment 3 => [3, 6, 4, 8, 8].
#  Max = 8. Min = 3.
#  Therefore, abs|Max - Min| = |8 - 3| = 5.

# print(minimumDifference([4, 6, 3, 1, 4], 5))  # 1
#  We can apply the atmost 5 operations in the following sequence.
#  Initial array => [4, 6, 3, 1, 4].
#    Increment 1 => [4, 6, 3, 2, 4].
#    Decrement 6 => [4, 5, 3, 2, 4].
#    Increment 2 => [4, 5, 3, 3, 4].
#    Decrement 5 => [4, 4, 3, 3, 4].
#    Increment 3 => [4, 4, 4, 3, 4].
#  Max = 4. Min = 3.
#  Therefore, abs|Max - Min| = |4 - 3| = 1.
