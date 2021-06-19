# Given a binary tree. Check whether the given tree is a Sum-binary Tree or not.
# Sum-binary Tree is a Binary Tree where the value of a every node
# is equal to sum of the nodes present in its left subtree and right subtree.
# An empty tree is Sum-binary Tree and sum of an empty tree can be considered as 0.
# A leaf node is also considered as SumTree.
# Return 1 if it sum-binary tree else return 0.
# 1 <= length of the array <= 100000
# 0 <= node values <= 50
# The only argument given is the root node of tree A.
# Return 1 if it is sum-binary tree else return 0.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isLeaf(self, node):
        if not node:
            return False

        if not node.left and not node.right:
            return True

        return False

    # @param A : root node of tree
    # @return an integer
    def solve(self, A):
        if not A or self.isLeaf(A):
            return 1

        if self.solve(A.left) and self.solve(A.right):
            if not A.left:
                leftSum = 0

            elif self.isLeaf(A.left):
                leftSum = A.left.val

            else:
                leftSum = 2 * A.left.val

            if not A.right:
                rightSum = 0

            elif self.isLeaf(A.right):
                rightSum = A.right.val

            else:
                rightSum = 2 * A.right.val

            if A.val == leftSum + rightSum:
                return 1

        return 0


bt = Solution()
T = TreeNode(26)
T.left = TreeNode(10)
T.left.left = TreeNode(4)
T.left.right = TreeNode(6)
T.right = TreeNode(3)
T.right.right = TreeNode(3)
print(bt.solve(T))  # 1

T = TreeNode(26)
T.left = TreeNode(10)
T.left.left = TreeNode(4)
T.left.right = TreeNode(6)
T.right = TreeNode(3)
T.right.right = TreeNode(4)
print(bt.solve(T))  # 0
