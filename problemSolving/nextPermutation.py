# Implement the next permutation, which rearranges numbers into
# the numerically next greater permutation of numbers for a given array A of size N.
# If such arrangement is not possible, it must be rearranged as the lowest possible order
# i.e., sorted in an ascending order.
# NOTE: The replacement must be in-place, do not allocate extra memory.
# DO NOT USE LIBRARY FUNCTION FOR NEXT PERMUTATION.
# Use of Library functions will disqualify your submission retroactively and will give you penalty points.
# 1 <= N <= 5 * 10^5
# 1 <= A[i] <= 10^9


class Solution:
    @staticmethod
    def nextPermutation(A):
        if len(A) <= 1:
            return A

        j = len(A) - 1

        while j >= 0 and A[j - 1] >= A[j]:
            j -= 1
        j -= 1

        while j >= 0:
            i = j+1
            while i < len(A) and A[j] < A[i]:
                i += 1
            A[i - 1], A[j] = A[j], A[i - 1]
            break

        A[j + 1:] = A[j + 1:][::-1]
        return A


result = Solution()
print(result.nextPermutation([1, 2, 3]))
print(result.nextPermutation([3, 2, 1]))
