# Given 3 array of integers A, B and C.
# A represents preorder traversal of a binary tree.
# B represents inorder traversal of a binary tree.
# C represents postorder traversal of a binary tree.
# Check whether these tree traversals are of the same tree or not.
# If they are of same tree return 1 else return 0.
# The arguments given are integer arrays A, B, and C.
# Return 1 if they are of same tree else return 0.
# 1 <= length of the array <= 1000
# all arrays are of same length
# 1 <= A[i], B[i], C[i] <= 10^9
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTreeInorderPostorder(self, A, B):
        root = TreeNode(B.pop())

        try:
            idx = A.index(root.val)
        except ValueError:
            return None

        if idx > 0:
            root.left = self.buildTreeInorderPostorder(A[:idx], B[:idx])

        if idx < len(A) - 1:
            root.right = self.buildTreeInorderPostorder(A[idx + 1:], B[idx:])

        return root

    def buildTreePreorderInorder(self, A, B):
        root = TreeNode(A.pop(0))

        try:
            idx = B.index(root.val)
        except ValueError:
            return None

        if idx > 0:
            root.left = self.buildTreePreorderInorder(A, B[:idx])

        if idx < len(B) - 1:
            root.right = self.buildTreePreorderInorder(A, B[idx + 1:])

        return root

    def isIdentical(self, A, B):
        if not A and not B:
            return True

        if not A or not B:
            return False

        if A.val == B.val \
                and self.isIdentical(A.left, B.left) \
                and self.isIdentical(A.right, B.right):
            return True

        return False

    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        if self.isIdentical(self.buildTreeInorderPostorder(B, C),
                            self.buildTreePreorderInorder(A, B)):
            return 1

        return 0


binaryTree = Solution()
print(binaryTree.solve([1, 2, 4, 5, 3], [4, 2, 5, 1, 3], [4, 5, 2, 3, 1]))  # 1
print(binaryTree.solve([1, 5, 4, 2, 3], [4, 2, 5, 1, 3], [4, 1, 2, 3, 5]))  # 0
