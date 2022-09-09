# Given a binary tree convert it into circular doubly linked list based on the following rules:
# The left and right pointers in nodes are to be used as previous and next pointers respectively
# in converted Circular Linked List.
# The order of nodes in List must be same as Inorder of the given Binary Tree.
# The first node of Inorder traversal must be the head node of the Circular List.
# NOTE: You are expected to convert the binary tree into Doubly linked list in place.
# 1 <= Number of nodes in tree <= 100000
# 1 <= Value of node <= 10^9
# The only argument given is the root pointer of the tree, A.
# Return the head pointer of the converted circular doubly linked list.
import sys
sys.setrecursionlimit(10**6)


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def concatenate(self, leftList, rightList):
        if not leftList:
            return rightList

        if not rightList:
            return leftList

        leftLast = leftList.left
        rightLast = rightList.left

        leftLast.right = rightList
        rightList.left = leftLast
        leftList.left = rightLast
        rightLast.right = leftList

        return leftList

    # @param A : root node of tree
    # @return the root node in the tree
    def solve(self, A):
        if not A:
            return None

        left = self.solve(A.left)
        right = self.solve(A.right)
        A.left = A
        A.right = A

        return self.concatenate(self.concatenate(left, A), right)


sol = Solution()
T = TreeNode(20)
T.left = TreeNode(8)
T.right = TreeNode(22)
print(sol.solve(T))

T = TreeNode(10)
T.left = TreeNode(8)
T.right = TreeNode(11)
print(sol.solve(T))
