# Given a binary tree A, flatten it to a linked list in-place.
# The left child of all nodes should be NULL.
# 1 <= size of tree <= 100000
# First and only argument is the head of tree A.
# Return the linked-list after flattening.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	def __init__(self):
		self.prev = None

	# @param A : root node of tree
	# @return the root node in the tree
	def flatten(self, A):
		if A:
			self.flatten(A.right)
			self.flatten(A.left)
			A.right = self.prev
			A.left = None
			self.prev = A

		return A


def printTree(BT):
	if BT.left:
		printTree(BT.left)

	print(BT.val, end=' ')

	if BT.right:
		printTree(BT.right)


bt = Solution()
T = TreeNode(1)
T.left = TreeNode(2)
T.right = TreeNode(3)
printTree(bt.flatten(T))
print()
T = TreeNode(1)
T.left = TreeNode(2)
T.left.left = TreeNode(3)
T.left.right = TreeNode(4)
T.right = TreeNode(5)
T.right.right = TreeNode(6)
printTree(bt.flatten(T))
