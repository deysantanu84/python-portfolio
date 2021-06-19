# Given a binary tree of integers denoted by root A.
# Return an array of integers representing the right view of the Binary tree.
# Right view of a Binary Tree is a set of nodes visible when the tree is visited from Right side.
# 1 <= Number of nodes in binary tree <= 100000
# 0 <= node values <= 10^9
# First and only argument is head of the binary tree A.
# Return an array, representing the right view of the binary tree.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, A):
        levels = [[A]]
        while any(levels[-1]):
            levels.append([x for node in levels[-1] for x in [node.left, node.right] if x])
        return [level[-1].val for level in levels[:-1]]


bt = Solution()
T = TreeNode(1)
T.left = TreeNode(2)
T.left.left = TreeNode(4)
T.left.left.left = TreeNode(8)
T.left.right = TreeNode(5)
T.right = TreeNode(3)
T.right.left = TreeNode(6)
T.right.right = TreeNode(7)
print(bt.solve(T))  # [1, 3, 7, 8]

T = TreeNode(1)
T.left = TreeNode(2)
T.left.right = TreeNode(4)
T.left.right.right = TreeNode(5)
T.right = TreeNode(3)
print(bt.solve(T))  # [1, 3, 4, 5]
