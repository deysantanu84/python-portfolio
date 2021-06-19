# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
# 1 <= number of nodes <= 10^5
# First and only argument is the root node of the binary tree.
# Return 0 / 1 ( 0 for false, 1 for true ).
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetricUtil(self, node1, node2):
        if not node1 and not node2:
            return 1

        elif not node1 or not node2:
            return 0

        else:
            if node1.val == node2.val \
                   and self.isSymmetricUtil(node1.left, node2.right) \
                   and self.isSymmetricUtil(node1.right, node2.left):
                return 1
            else:
                return 0

    # @param A : root node of tree
    # @return an integer
    def isSymmetric(self, A):
        if not A:
            return 1

        return self.isSymmetricUtil(A.left, A.right)


binaryTree = Solution()
T = TreeNode(1)
T.left = TreeNode(2)
T.left.right = TreeNode(3)
T.right = TreeNode(2)
T.right.right = TreeNode(3)
print(binaryTree.isSymmetric(T))  # 0

T = TreeNode(1)
T.left = TreeNode(2)
T.left.left = TreeNode(3)
T.left.right = TreeNode(4)
T.right = TreeNode(2)
T.right.left = TreeNode(4)
T.right.right = TreeNode(3)
print(binaryTree.isSymmetric(T))  # 1
