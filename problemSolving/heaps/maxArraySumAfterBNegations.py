# Given an array of integers A and an integer B. You must modify the array exactly B number of times.
# In single modification, we can replace any one array element A[i] by -A[i].
# You need to perform these modifications in such a way that after exactly B modifications,
# sum of the array must be maximum.
# 1 <= length of the array <= 5*10^5
# 1 <= B <= 5 * 10^6
# -100 <= A[i] <= 100
# First argument given is an integer array A.
# Second argument given is an integer B.
# Return an integer denoting the maximum array sum after B modifications.
import sys
INT_MAX = sys.maxsize - 1


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        result = 0
        A.sort()
        minVal = INT_MAX
        for item in A:
            if B and item < 0:
                item = -item
                B -= 1

            minVal = min(minVal, item)
            result += item

        if B:
            B %= 2

        if B:
            result -= 2 * minVal

        return result


sol = Solution()
print(sol.solve([24, -68, -29, -9, 84], 4))  # 196
print(sol.solve([57, 3, -14, -87, 42, 38, 31, -7, -28, -61], 10))  # 362
