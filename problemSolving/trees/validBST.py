# Given a binary tree represented by root A.
# Assume a BST is defined as follows:
# 1) The left subtree of a node contains only nodes with keys less than the node's key.
# 2) The right subtree of a node contains only nodes with keys greater than the node's key.
# 3) Both the left and right subtrees must also be binary search trees.
# 1 <= Number of nodes in binary tree <= 100000
# 0 <= node values <= 10^9
# First and only argument is head of the binary tree A.
# Return 0 if false and 1 if true.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return an integer
    def isValidBST(self, A):
        # Iterative
        if not A:
            return 1

        stack = [(A, -float('inf'), float('inf'))]

        while len(stack):
            node, left, right = stack.pop()
            if node.val <= left or node.val >= right:
                return 0

            if node.left:
                stack.append((node.left, left, node.val))

            if node.right:
                stack.append((node.right, node.val, right))

        return 1

    # Recursive
    def recursive(self, root):
        def rec(node, left, right):
            if node:
                if node.val <= left or node.val >= right:
                    return 0
                return rec(node.left, left, node.val) and rec(node.right, node.val, right)
            return 1

        return rec(root, -float('inf'), float('inf'))


bst = Solution()
T = TreeNode(1)
T.left = TreeNode(2)
T.right = TreeNode(3)
print(bst.isValidBST(T))  # 0
print(bst.recursive(T))  # 0

T = TreeNode(2)
T.left = TreeNode(1)
T.right = TreeNode(3)
print(bst.isValidBST(T))  # 1
print(bst.recursive(T))  # 1
