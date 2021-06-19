# Given a binary search tree represented by root A,
# write a function to find the Bth smallest element in the tree.
# 1 <= Number of nodes in binary tree <= 100000
# 0 <= node values <= 10^9
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	# @param A : root node of tree
	# @param B : integer
	# @return an integer
	def kthsmallest(self, A, B):
		stack = []
		result = []
		temp = A

		while stack or temp:
			while temp:
				stack.append(temp)
				temp = temp.left

			temp = stack.pop()
			result.append(temp)
			temp = temp.right

		return result[B - 1].val


bst = Solution()
T = TreeNode(2)
T.left = TreeNode(1)
T.right = TreeNode(3)
print(bst.kthsmallest(T, 2))  # 2

T = TreeNode(3)
T.left = TreeNode(2)
T.left.left = TreeNode(1)
print(bst.kthsmallest(T, 1))  # 1
