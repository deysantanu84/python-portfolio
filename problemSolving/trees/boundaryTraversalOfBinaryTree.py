# Given a binary tree, return the values of its boundary in anti-clockwise direction
# starting from the root. Boundary includes left boundary, leaves, and right boundary in order
# without duplicate nodes.
# Left boundary is defined as the path from the root to the left-most node.
# Right boundary is defined as the path from the root to the right-most node.
# If the root doesn't have left subtree or right subtree, then the root itself is left boundary
# or right boundary. Note this definition only applies to the input binary tree, and not applies
# to any subtrees.
# The left-most node is defined as a leaf node you could reach when you always firstly travel to
# the left subtree if exists. If not, travel to the right subtree. Repeat until you reach a leaf node.
# The right-most node is also defined by the same way with left and right exchanged.
# Return an array of integers denoting the boundary values of tree in anti-clockwise order.
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# TLE
class Solution1:
    def inorder(self, root, result):
        if not root:
            return

        self.inorder(root.left, result)

        if not root.left and not root.right:
            result.append(root.val)

        self.inorder(root.right, result)

    # @param A : root node of tree
    # @return a list of integers
    def solve(self, A):
        result = []
        curr = A
        while curr.left and curr.right:
            while curr.left:
                result.append(curr.val)
                curr = curr.left

            if curr.right:
                curr = curr.right
                result.append(curr.val)

        rightBoundary = []
        curr = A
        while curr.left and curr.right:
            while curr.right:
                curr = curr.right
                rightBoundary.append(curr.val)

            if curr.left:
                curr = curr.left
                rightBoundary.append(curr.val)

        curr = A
        self.inorder(curr, result)
        rightBoundary.reverse()

        result.extend(rightBoundary[1:])

        return result


class Solution:
    def traverseLeaves(self, root, result):
        if root:
            self.traverseLeaves(root.left, result)

            if not root.left and not root.right:
                result.append(root.val)

            self.traverseLeaves(root.right, result)

    def traverseLeftBoundary(self, root, result):
        if root:
            if root.left:
                result.append(root.val)
                self.traverseLeftBoundary(root.left, result)

            elif root.right:
                result.append(root.val)
                self.traverseLeftBoundary(root.right, result)

    def traverseRightBoundary(self, root, result):
        if root:
            if root.right:
                self.traverseRightBoundary(root.right, result)
                result.append(root.val)

            elif root.left:
                self.traverseRightBoundary(root.left, result)
                result.append(root.val)

    # @param A : root node of tree
    # @return a list of integers
    def solve(self, A):
        result = []

        if A:
            result.append(A.val)
            self.traverseLeftBoundary(A.left, result)
            self.traverseLeaves(A.left, result)
            self.traverseLeaves(A.right, result)
            self.traverseRightBoundary(A.right, result)

        return result


sol = Solution()
T = TreeNode(1)
T.left = TreeNode(2)
T.left.left = TreeNode(4)
T.left.right = TreeNode(5)
T.left.right.left = TreeNode(7)
T.left.right.right = TreeNode(8)
T.right = TreeNode(3)
T.right.left = TreeNode(6)
T.right.left.left = TreeNode(9)
T.right.left.right = TreeNode(10)
print(sol.solve(T))  # [1, 2, 4, 7, 8, 9, 10, 6, 3]

T = TreeNode(1)
T.left = TreeNode(2)
T.left.left = TreeNode(4)
T.left.right = TreeNode(5)
T.right = TreeNode(3)
T.right.left = TreeNode(6)
T.right.right = TreeNode(7)
print(sol.solve(T))  # [1, 2, 4, 5, 6, 7, 3]
