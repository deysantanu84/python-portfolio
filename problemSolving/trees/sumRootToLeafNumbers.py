# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
# An example is the root-to-leaf path 1->2->3 which represents the number 123.
# Find the total sum of all root-to-leaf numbers % 1003.
# The root-to-leaf path 1->2 represents the number 12. The root-to-leaf path 1->3 represents the number 13.
# Return the sum = (12 + 13) % 1003 = 25 % 1003 = 25.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	def calculateNodeSum(self, node, result=0):
		if not node:
			return 0

		result = (result * 10 + node.val) % 1003

		if not node.left and not node.right:
			return result

		return (self.calculateNodeSum(node.left, result) + self.calculateNodeSum(node.right, result)) % 1003

	# @param A : root node of tree
	# @return an integer
	def sumNumbers(self, A):
		return self.calculateNodeSum(A)


bst = Solution()
T = TreeNode(1)
T.left = TreeNode(2)
T.right = TreeNode(3)
print(bst.sumNumbers(T))  # 25
