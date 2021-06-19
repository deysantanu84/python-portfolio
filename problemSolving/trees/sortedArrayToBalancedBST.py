# Given an array where elements are sorted in ascending order,
# convert it to a height Balanced Binary Search Tree (BBST).
# Balanced tree : a height-balanced binary tree is defined as a binary tree
# in which the depth of the two subtrees of every node never differ by more than 1.
# 1 <= length of array <= 100000
# First argument is an integer array A.
# Return a root node of the Binary Search Tree.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : tuple of integers
    # @return the root node in the tree
    def sortedArrayToBST(self, A):
        if not A:
            return None

        mid = len(A) // 2

        root = TreeNode(A[mid])
        root.left = self.sortedArrayToBST(A[:mid])
        root.right = self.sortedArrayToBST(A[mid + 1:])

        return root


def printTree(BT):
    if BT.left:
        printTree(BT.left)

    print(BT.val, end=' ')

    if BT.right:
        printTree(BT.right)


bst = Solution()
printTree(bst.sortedArrayToBST([1, 2, 3]))
print()
printTree(bst.sortedArrayToBST([1, 2, 3, 5, 10]))
