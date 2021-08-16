# Given an integer A.
# Two numbers X and Y are defined as follows:
# X is the greatest number smaller than A such that XOR sum of X and A is the same as the sum of X and A.
# Y is the smallest number greater than A such that XOR sum of Y and A is the same as the sum of Y and A.
# Find and return the XOR of X and Y.
# NOTE 1: XOR of X and Y is defined as X ^ Y where '^' is the BITWISE XOR operator.
# NOTE 2: Your code will be run against a maximum of 100000 Test Cases.
# 1 <= A <= 10^9
# First and only argument is an integer A.
# Return an integer denoting the XOR of X and Y.
from math import log2


class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        temp = int(log2(A)) + 1
        m = 0

        for i in range(0, temp):
            if A & (1 << i):
                continue
            else:
                m += (1 << i)

        n = (1 << temp)
        return m ^ n


sol = Solution()
print(sol.solve(5))  # 10
