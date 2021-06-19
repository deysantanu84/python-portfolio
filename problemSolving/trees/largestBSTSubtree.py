# Given a Binary Tree A with N nodes.
# Write a function that returns the size of the largest subtree which is also a Binary Search Tree (BST).
# If the complete Binary Tree is BST, then return the size of whole tree.
# NOTE:
# Largest subtree means subtree with most number of nodes.
# 1 <= N <= 10^5
# First and only argument is an pointer to root of the binary tree A.
# Return an single integer denoting the size of the largest subtree which is also a BST.
import sys

INT_MIN = - sys.maxsize
INT_MAX = sys.maxsize - 1


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def largestBSTSubtreeUtil(self, A):
        if not A:
            return 0, INT_MIN, INT_MAX, 0, True

        if not A.left and not A.right:
            return 1, A.val, A.val, 1, True

        left = self.largestBSTSubtreeUtil(A.left)
        right = self.largestBSTSubtreeUtil(A.right)

        result = [0, 0, 0, 0, 0]
        result[0] = (1 + left[0] + right[0])

        if left[4] and right[4] and left[1] < A.val < right[2]:

            result[2] = min(left[2], min(right[2], A.val))
            result[1] = max(right[1], max(left[1], A.val))

            result[3] = result[0]
            result[4] = True

            return result

        result[3] = max(left[3], right[3])
        result[4] = False

        return result

    # @param A : root node of tree
    # @return an integer
    def solve(self, A):
        return self.largestBSTSubtreeUtil(A)[3]


bst = Solution()
T = TreeNode(10)
T.left = TreeNode(5)
T.left.left = TreeNode(1)
T.left.right = TreeNode(8)
T.right = TreeNode(15)
T.right.right = TreeNode(7)
print(bst.solve(T))  # 3

T = TreeNode(5)
T.left = TreeNode(3)
T.left.left = TreeNode(1)
T.left.right = TreeNode(4)
T.right = TreeNode(8)
T.right.left = TreeNode(7)
T.right.right = TreeNode(9)
print(bst.solve(T))  # 7

T = TreeNode(20)
T.left = TreeNode(12)
T.left.left = TreeNode(6)
T.left.right = TreeNode(18)
T.right = TreeNode(34)
T.right.left = TreeNode(30)
T.right.right = TreeNode(21)
print(bst.solve(T))  # 3
