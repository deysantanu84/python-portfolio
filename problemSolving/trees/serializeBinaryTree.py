# Given the root node of a Binary Tree denoted by A.
# You have to Serialize the given Binary Tree in the described format.
# Serialize means encode it into a integer array denoting the Level Order Traversal of the given Binary Tree.
# NOTE:
# In the array, the NULL/None child is denoted by -1.
# For more clarification check the Example Input.
# 1 <= number of nodes <= 10^5
# Only argument is a A denoting the root node of a Binary Tree.
# Return an integer array denoting the Level Order Traversal of the given Binary Tree.
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, A):
        result = []
        queue = deque([A])

        while queue:
            node = queue.pop()
            if node:
                result.append(node.val)
                queue.appendleft(node.left)
                queue.appendleft(node.right)

            else:
                result.append(-1)

        return result


binaryTree = Solution()
T = TreeNode(1)
T.left = TreeNode(2)
T.left.left = TreeNode(4)
T.left.right = TreeNode(5)
T.right = TreeNode(3)
print(binaryTree.solve(T))  # [1, 2, 3, 4, 5, -1, -1, -1, -1, -1, -1]

T.right.right = TreeNode(6)
print(binaryTree.solve(T))  # [1, 2, 3, 4, 5, -1, 6, -1, -1, -1, -1, -1, -1]
