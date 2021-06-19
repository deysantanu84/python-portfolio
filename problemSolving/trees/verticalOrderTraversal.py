# Given a binary tree, return a 2-D array with vertical order traversal of it.
# Go through the example and image for more details.
# NOTE: If 2 Tree Nodes shares the same vertical level then the one with lesser depth will come first.
# 0 <= number of nodes <= 10^5
# First and only argument is a pointer to the root node of binary tree, A.
# Return a 2D array denoting the vertical order traversal of tree as shown.
from collections import OrderedDict


class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	# @param A : root node of tree
	# @return a list of list of integers
	def verticalOrderTraversal(self, A):
		if not A:
			return

		queue = []
		nodeMap = {}
		horizontalDistanceMap = {}

		queue.append(A)
		horizontalDistanceMap[A] = 0
		nodeMap[0] = [A.val]

		while len(queue) > 0:
			temp = queue.pop(0)

			if temp.left:
				queue.append(temp.left)
				horizontalDistanceMap[temp.left] = horizontalDistanceMap[temp] - 1
				horizontalDistance = horizontalDistanceMap[temp.left]

				if horizontalDistance not in nodeMap:
					nodeMap[horizontalDistance] = []

				nodeMap[horizontalDistance].append(temp.left.val)

			if temp.right:
				queue.append(temp.right)
				horizontalDistanceMap[temp.right] = horizontalDistanceMap[temp] + 1
				horizontalDistance = horizontalDistanceMap[temp.right]

				if horizontalDistance not in nodeMap:
					nodeMap[horizontalDistance] = []

				nodeMap[horizontalDistance].append(temp.right.val)

		sortedMap = OrderedDict(sorted(nodeMap.items()))

		result = []
		for i in sortedMap.values():
			result.append(i)

		return result


binaryTree = Solution()
T = TreeNode(6)
T.left = TreeNode(3)
T.left.left = TreeNode(2)
T.left.right = TreeNode(5)
T.right = TreeNode(7)
T.right.right = TreeNode(9)
print(binaryTree.verticalOrderTraversal(T))  # [[2], [3], [6, 5], [7], [9]]

T = TreeNode(1)
T.left = TreeNode(3)
T.left.left = TreeNode(2)
T.right = TreeNode(7)
T.right.right = TreeNode(9)
print(binaryTree.verticalOrderTraversal(T))  # [[2], [3], [1], [7], [9]]
