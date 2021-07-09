# The monetary system in DarkLand is really simple and systematic. The locals only use coins.
# The coins come in different values. The values used are:
#  1, 5, 25, 125, 625, 3125, 15625, ...
# Formally, for each K >= 0 there are coins worth 5^K.
# Given an integer A denoting the cost of an item, find and return the smallest number of coins
# necessary to pay exactly the cost of the item (assuming you have a sufficient supply of coins of
# each of the types you will need).
# 1 <= A <= 2*10^9
# The only argument given is integer A.
# Return the smallest number of coins necessary to pay exactly the cost of the item.
from math import log


class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        pass


sol = Solution()
print(sol.solve(47))  # 7
print(sol.solve(9))  # 5
