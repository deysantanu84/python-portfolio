# Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest path from the root
# node down to the nearest leaf node.
# NOTE : The path has to end on a leaf node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	# @param A : root node of tree
	# @return an integer
	def minDepth(self, A):
		if not A:
			return 0

		if not A.left and not A.right:
			return 1

		elif not A.right:
			return self.minDepth(A.left) + 1

		elif not A.left:
			return self.minDepth(A.right) + 1

		else:
			return min(map(self.minDepth, (A.left, A.right))) + 1


bt = Solution()
T = TreeNode(1)
T.left = TreeNode(2)
print(bt.minDepth(T))  # 2
