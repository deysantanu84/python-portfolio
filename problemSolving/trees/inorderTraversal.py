# Given a binary tree, return the inorder traversal of its nodes values.
# NOTE: Using recursion is not allowed.
# 1 <= number of nodes <= 10^5
# First and only argument is root node of the binary tree, A.
# Return an integer array denoting the inorder traversal of the given binary tree.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	# @param A : root node of tree
	# @return a list of integers
	def inorderTraversal(self, A):
		result = []
		temp = [(A, False)]

		while temp:
			node, visited = temp.pop()

			if node:
				if visited:
					result.append(node.val)

				else:
					temp.append((node.right, False))
					temp.append((node, True))
					temp.append((node.left, False))

		return result


binaryTree = Solution()
T = TreeNode(1)
T1 = TreeNode(2)
T2 = TreeNode(3)
T.right = T1
T1.left = T2
print(binaryTree.inorderTraversal(T))  # [1, 3, 2]

T3 = TreeNode(6)
T.left = T3
print(binaryTree.inorderTraversal(T))  # [6, 1, 3, 2]
