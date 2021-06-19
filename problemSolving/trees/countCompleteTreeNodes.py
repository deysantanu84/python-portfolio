# Given a complete binary tree, A, find the total number of nodes in the tree.
# The first and the only argument of input contains a reference to the root of the complete binary tree.
# Return an integer representing the number of nodes in the complete binary tree.
# 1 <= Number of nodes in the binary tree <= 1e5
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def depthLeft(self, node):
        depth = 0
        while node:
            depth += 1
            node = node.left
        return depth

    def depthRight(self, node):
        depth = 0
        while node:
            depth += 1
            node = node.right
        return depth

    # @param A : root node of tree
    # @return an integer
    def solve(self, A):
        if not A:
            return 0

        leftDepth = self.depthLeft(A.left)
        rightDepth = self.depthRight(A.right)

        if leftDepth == rightDepth:
            return 2**(leftDepth + 1) - 1

        else:
            return 1 + self.solve(A.left) + self.solve(A.right)


tree = Solution()
T = TreeNode(1)
T.left = TreeNode(2)
T.right = TreeNode(3)
print(tree.solve(T))  # 3

T = TreeNode(1)
T.left = TreeNode(2)
T.left.left = TreeNode(4)
T.left.right = TreeNode(5)
T.right = TreeNode(3)
print(tree.solve(T))  # 5
