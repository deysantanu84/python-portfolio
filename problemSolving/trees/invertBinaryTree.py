# Given a binary tree A, invert the binary tree and return it.
# Inverting refers to making left child as the right child and vice versa.
# 1 <= size of tree <= 100000
# First and only argument is the head of the tree A.
# Return the head of the inverted tree.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	# @param A : root node of tree
	# @return the root node in the tree
	def invertTree(self, A):
		A.left, A.right = A.right, A.left

		if A.left:
			self.invertTree(A.left)

		if A.right:
			self.invertTree(A.right)

		return A


def printTree(BT):
	if BT.left:
		printTree(BT.left)

	print(BT.val, end=' ')

	if BT.right:
		printTree(BT.right)


binaryTree = Solution()
T = TreeNode(1)
T.left = TreeNode(2)
T.right = TreeNode(3)
printTree(T)
print()
printTree(binaryTree.invertTree(T))
print()

T = TreeNode(1)
T.left = TreeNode(2)
T.right = TreeNode(3)
T.left.left = TreeNode(4)
T.left.right = TreeNode(5)
T.right.left = TreeNode(6)
T.right.right = TreeNode(7)
printTree(T)
print()
printTree(binaryTree.invertTree(T))
print()
