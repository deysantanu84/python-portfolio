# Given two binary trees, check if they are equal or not.
# Two binary trees are considered equal if they are structurally
# identical and the nodes have the same value.
# 1 <= number of nodes <= 10^5
# First argument is a root node of first tree, A.
# Second argument is a root node of second tree, B.
# Return 0 / 1 ( 0 for false, 1 for true ) for this problem.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @param B : root node of tree
    # @return an integer
    def isSameTree(self, A, B):
        if not A and not B:
            return 1

        elif not A or not B:
            return 0

        else:
            if A.val == B.val \
                    and self.isSameTree(A.left, B.left) \
                    and self.isSameTree(A.right, B.right):
                return 1
            else:
                return 0


binaryTree = Solution()
T = TreeNode(1)
T.left = TreeNode(2)
T.right = TreeNode(3)
print(binaryTree.isSameTree(T, T))  # 1

R = TreeNode(1)
R.left = TreeNode(3)
R.right = TreeNode(3)
print(binaryTree.isSameTree(T, R))  # 0
