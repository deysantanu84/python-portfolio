# Given an integer A, how many structurally unique BST's (binary search trees)
# exist that can store values 1...A?
# 1 <= A <=18
# First and only argument is the integer A
# Return a single integer, the answer to the problem
class Solution:
    # @param A : integer
    # @return an integer
    def numTrees(self, A):
        resultList = [0] * (A + 1)
        resultList[0] = 1

        for i in range(1, A + 1):
            for j in range(i):
                resultList[i] += resultList[j] * resultList[i - 1 - j]

        return resultList[A]


sol = Solution()
print(sol.numTrees(1))  # 1
print(sol.numTrees(2))  # 2
