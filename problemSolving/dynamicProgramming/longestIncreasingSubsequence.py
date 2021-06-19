# Find the longest increasing subsequence of a given array of integers, A.
# In other words, find a subsequence of array in which the subsequence's
# elements are in strictly increasing order, and in which the subsequence is as long as possible.
# In this case, return the length of the longest increasing subsequence.
# 0 <= length(A) <= 2500
# 1 <= A[i] <= 2500
# The first and the only argument is an integer array A.
# Return an integer representing the length of the longest increasing subsequence.
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def lis(self, A):
        if not A:
            return 0

        resultList = [1] * len(A)

        for i in range(1, len(A)):
            for j in range(i):
                if A[i] > A[j]:
                    resultList[i] = max(resultList[i], resultList[j] + 1)

        return max(resultList)


sol = Solution()
print(sol.lis([1, 2, 1, 5]))  # 3
print(sol.lis([2, 1, 4, 3]))  # 2
print(sol.lis([5, 6, 3, 7, 9]))  # 4
print(sol.lis([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))  # 6
