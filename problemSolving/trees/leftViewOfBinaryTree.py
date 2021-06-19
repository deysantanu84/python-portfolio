# Given a binary tree of integers.
# Return an array of integers representing the left view of the Binary tree.
# Left view of a Binary Tree is a set of nodes visible when the tree is visited from Left side
# NOTE: The value comes first in the array which have lower level.
# 1 <= Number of nodes in binary tree <= 100000
# 0 <= node values <= 10^9
# First and only argument is a root node of the binary tree, A.
# Return an integer array denoting the left view of the Binary tree.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def leftViewUtil(self, root, level, maxLevel, result):
        if root is None:
            return

        if maxLevel[0] < level:
            result.append(root.val)
            maxLevel[0] = level

        self.leftViewUtil(root.left, level + 1, maxLevel, result)
        self.leftViewUtil(root.right, level + 1, maxLevel, result)

    # @param A : root node of tree
    # @return a list of integers
    def solve(self, A):
        result = []
        maxLevel = [0]
        self.leftViewUtil(A, 1, maxLevel, result)
        return result


bt = Solution()
T = TreeNode(1)
T.left = TreeNode(2)
T.left.left = TreeNode(4)
T.left.left.left = TreeNode(8)
T.left.right = TreeNode(5)
T.right = TreeNode(3)
T.right.left = TreeNode(6)
T.right.right = TreeNode(7)
print(bt.solve(T))  # [1, 2, 4, 8]

T = TreeNode(1)
T.left = TreeNode(2)
T.left.right = TreeNode(4)
T.left.right.right = TreeNode(5)
T.right = TreeNode(3)
print(bt.solve(T))  # [1, 2, 4, 5]
