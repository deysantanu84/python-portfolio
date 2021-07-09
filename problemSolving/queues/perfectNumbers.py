# Given an integer A, you have to find the Ath Perfect Number.
# A Perfect Number has the following properties:
# It comprises only 1 and 2.
# The number of digits in a Perfect number is even.
# It is a palindrome number.
# For example 11, 22, 112211 are Perfect numbers, where 123, 121, 782, 1 are not.
# 1 <= A <= 100000
# The only argument given is an integer A.
# Return a string that denotes the Ath Perfect Number.
from math import ceil, log2


class Solution:
    # @param A : integer
    # @return a strings
    def solve(self, A):
        length = ceil(log2(A + 2)) - 1
        rank = A - (1 << length) + 1
        left = ""
        right = ""

        for i in range(length - 1, -1, -1):
            mask = (1 << i)
            bit = (mask & rank)
            if bit:
                left += '2'
                right += '2'
            else:
                left += '1'
                right += '1'

        right = right[::-1]
        result = left + right

        return result


sol = Solution()
print(sol.solve(2))  # 22
print(sol.solve(3))  # 1111
