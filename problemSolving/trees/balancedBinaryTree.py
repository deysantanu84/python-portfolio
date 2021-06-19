# Given a root of binary tree A, determine if it is height-balanced.
# A height-balanced binary tree is defined as a binary tree in which
# the depth of the two subtrees of every node never differ by more than 1.
# 1 <= size of tree <= 100000
# First and only argument is the root of the tree A.
# Return 0 / 1 ( 0 for false, 1 for true ) for this problem.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def depth(self, node):
        if not node:
            return 0

        return max(self.depth(node.left), self.depth(node.right)) + 1

    # @param A : root node of tree
    # @return an integer
    def isBalanced(self, A):
        if not A:
            return 1

        if (abs(self.depth(A.left) - self.depth(A.right)) < 2) \
                and self.isBalanced(A.left) \
                and self.isBalanced(A.right):
            return 1

        else:
            return 0


bst = Solution()
T = TreeNode(1)
T.left = TreeNode(2)
T.right = TreeNode(3)
print(bst.isBalanced(T))  # 1

T = TreeNode(1)
T.left = TreeNode(2)
T.left.left = TreeNode(3)
print(bst.isBalanced(T))  # 0
