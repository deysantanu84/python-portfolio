# You are given an array A. You need to find the length of the Longest Increasing Subsequence in the array.
# In other words, you need to find a subsequence of array A in which the elements are in sorted order,
# (strictly increasing) and as long as possible.
# 1 ≤ length(A), A[i] ≤ 10^5
# The first and only argument of the input is the array A.
# Output a single integer, the length of the longest increasing subsequence in array A.
from bisect import bisect_left


class Solution:
    # @param A : list of integers
    # @return an integer
    def findLIS(self, A):
        result = [A[0]]

        for i in range(1, len(A)):
            if A[i] > result[-1]:
                result.append(A[i])

            else:
                temp = bisect_left(result, A[i])
                result[temp] = A[i]

        return len(result)


sol = Solution()
print(sol.findLIS([2, 1, 4, 3]))  # 2
print(sol.findLIS([5, 6, 3, 7, 9]))  # 4
