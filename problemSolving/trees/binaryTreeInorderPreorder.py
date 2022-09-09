# Given preorder and inorder traversal of a tree, construct the binary tree.
# NOTE: You may assume that duplicates do not exist in the tree.
# 1 <= number of nodes <= 10^5
# First argument is an integer array A denoting the preorder traversal of the tree.
# Second argument is an integer array B denoting the inorder traversal of the tree.
# Return the root node of the binary tree.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return the root node in the tree
    def buildTree(self, A, B):
        idx = B.index(A.pop(0))
        root = TreeNode(B[idx])

        if idx > 0:
            root.left = self.buildTree(A, B[:idx])

        if idx < len(B) - 1:
            root.right = self.buildTree(A, B[idx + 1:])

        return root


def printTree(BT):
    if BT.left:
        printTree(BT.left)

    print(BT.val, end=' ')

    if BT.right:
        printTree(BT.right)


binaryTree = Solution()
printTree(binaryTree.buildTree([1, 2, 3], [2, 1, 3]))
print()
printTree(binaryTree.buildTree([1, 6, 2, 3], [6, 1, 3, 2]))
print()
