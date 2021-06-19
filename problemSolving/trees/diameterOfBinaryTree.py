# Given a Binary Tree A consisting of N integer nodes, you need to find the diameter of the tree.
# The diameter of a tree is the number of edges on the longest path between two nodes in the tree.
# 0 <= N <= 10^5
# First and only Argument represents the root of binary tree A.
# Return an single integer denoting the diameter of the tree.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	def __init__(self):
		self.diameter = 0

	def depthFirstSearch(self, node):
		if not node:
			return 0

		leftHeight = self.depthFirstSearch(node.left)
		rightHeight = self.depthFirstSearch(node.right)
		self.diameter = max(self.diameter, leftHeight + rightHeight)
		return max(leftHeight, rightHeight) + 1

	# @param A : root node of tree
	# @return an integer
	def solve(self, A):
		self.diameter = 0
		self.depthFirstSearch(A)
		return self.diameter


binaryTree = Solution()
T = TreeNode(1)
T.left = TreeNode(2)
T.left.left = TreeNode(4)
T.left.right = TreeNode(5)
T.right = TreeNode(3)
print(binaryTree.solve(T))  # 3

T.right.right = TreeNode(6)
print(binaryTree.solve(T))  # 4
