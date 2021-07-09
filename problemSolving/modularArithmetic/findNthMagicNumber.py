# Given an integer A, find and return the Ath magic number.
# A magic number is defined as a number which can be expressed as a power of 5 or sum of unique powers of 5.
# First few magic numbers are 5, 25, 30(5 + 25), 125, 130(125 + 5), ….
# 1 <= A <= 5000
# The only argument given is integer A.
# Return the Ath magic number.
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        result = 0
        power = 1

        while A:
            power *= 5
            if A & 1:
                result += power

            A >>= 1

        return result


sol = Solution()
print(sol.solve(3))  # 30
print(sol.solve(10))  # 650
