# Given an integer A, return the number of trailing zeroes in A! i.e. factorial of A.
# Note: Your solution should run in logarithmic time complexity.
# 1 <= A <= 10^9
# First and only argument is a single integer A.
# Return a single integer denoting number of zeroes.
class Solution:
    # @param A : integer
    # @return an integer
    def trailingZeroes(self, A):
        result = 0
        i = 5

        while A // i >= 1:
            result += A // i
            i *= 5

        return result


sol = Solution()
print(sol.trailingZeroes(5))  # 1
print(sol.trailingZeroes(6))  # 1
