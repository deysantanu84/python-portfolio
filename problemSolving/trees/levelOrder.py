# Given a binary tree, return the level order traversal of its nodes' values.
# (ie, from left to right, level by level).
# 1 <= number of nodes <= 10^5
# First and only argument is root node of the binary tree, A.
# Return a 2D integer array denoting the level order traversal of the given binary tree.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param A : root node of tree
	# @return a list of list of integers
	def levelOrder(self, A):
		if not A:
			return A

		queue = [A]
		result = []

		while len(queue) > 0:
			level = []
			N = len(queue)

			for _ in range(N):
				node = queue.pop(0)
				level.append(node.val)

				if node.left:
					queue.append(node.left)

				if node.right:
					queue.append(node.right)

			result.append(level)

		return result


bt = Solution()
T = TreeNode(3)
T.left = TreeNode(9)
T.right = TreeNode(20)
T.right.left = TreeNode(15)
T.right.right = TreeNode(7)
print(bt.levelOrder(T))  # [[3], [9, 20], [15, 7]]

T = TreeNode(1)
T.left = TreeNode(6)
T.right = TreeNode(2)
T.right.left = TreeNode(3)
print(bt.levelOrder(T))  # [[1], [6, 2], [3]]
