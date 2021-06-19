# Given an integer array A of size N.
# Find the contiguous subarray within the given array (containing at least one number)
# which has the largest product.
# Return an integer corresponding to the maximum product possible.
# NOTE: Answer will fit in 32-bit integer value.
# 1 <= N <= 5 * 10^5
# -100 <= A[i] <= 100
# First and only argument is an integer array A.
# Return an integer corresponding to the maximum product possible.
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProduct(self, A):
        result = A[0]
        overallMax = A[0]
        overallMin = A[0]

        for index, val in enumerate(A[1:], start=1):
            prevMin = overallMin
            overallMin = min(overallMin * val, overallMax * val, val)
            overallMax = max(prevMin * val, overallMax * val, val)
            result = max(overallMax, result)

        return result


sol = Solution()
print(sol.maxProduct([4, 2, -5, 1]))  # 8
print(sol.maxProduct([-3, 0, -5, 0]))  # 0
