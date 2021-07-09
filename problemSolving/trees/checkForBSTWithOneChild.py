# Given preorder traversal of a binary tree, check if it is possible that it is also a preorder
# traversal of a Binary Search Tree (BST), where each internal node (non-leaf nodes) have exactly one child.
# 1 <= number of nodes <= 100000
# First and only argument is an integer array denoting the preorder traversal of binary tree.
# Return a string "YES" if true else "NO".
class Solution:
    # @param A : list of integers
    # @return a strings
    def solve(self, A):
        N = len(A)

        if A[N - 1] > A[N - 2]:
            maxVal = A[N - 1]
            minVal = A[N - 2]
        else:
            maxVal = A[N - 2]
            minVal = A[N - 1]

        for i in range(N - 3, -1, -1):
            if A[i] < minVal:
                minVal = A[i]
            elif A[i] > maxVal:
                maxVal = A[i]
            else:
                return "NO"

        return "YES"


sol = Solution()
print(sol.solve([4, 10, 5, 8]))  # "YES"
print(sol.solve([1, 5, 6, 4]))  # "NO"
