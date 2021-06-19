# You are given the root node of a binary tree A, You have to find the height of the given tree.
# A binary tree's height is the number of nodes along the
# longest path from the root node down to the farthest leaf node.
# 1 <= Number of nodes in the tree <= 10^5
# 0 <= Value of each node <= 10^9
# First and only argument is a tree node A.
# Return an integer denoting the height of the tree.
import sys
sys.setrecursionlimit(10**6)


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):
        if not A:
            return 0

        else:
            leftDepth = self.solve(A.left)
            rightDepth = self.solve(A.right)
            return max(leftDepth, rightDepth) + 1


bt = Solution()
T = TreeNode(1)
T.left = TreeNode(4)
T.right = TreeNode(3)
print(bt.solve(T))  # 2

T = TreeNode(1)
T.left = TreeNode(4)
T.left.left = TreeNode(2)
T.right = TreeNode(3)
print(bt.solve(T))  # 3
