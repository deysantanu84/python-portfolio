# Given a binary tree and a sum, determine if the tree has a root-to-leaf path
# such that adding up all the values along the path equals the given sum.
# 1 <= number of nodes <= 10^5
# -100000 <= B, value of nodes <= 100000
# First argument is a root node of the binary tree, A.
# Second argument is an integer B denoting the sum.
# Return 1, if there exist root-to-leaf path such that adding up all the values
# along the path equals the given sum. Else, return 0.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def hasPathSum(self, A, B):
        if not A:
            return 0

        if not A.left and not A.right:
            if A.val == B:
                return 1
            else:
                return 0

        if self.hasPathSum(A.left, B - A.val) \
                or self.hasPathSum(A.right, B - A.val):
            return 1
        else:
            return 0


bst = Solution()
T = TreeNode(5)
T.left = TreeNode(4)
T.left.left = TreeNode(11)
T.left.left.left = TreeNode(7)
T.left.left.right = TreeNode(2)
T.right = TreeNode(8)
T.right.left = TreeNode(13)
T.right.right = TreeNode(4)
T.right.right.right = TreeNode(1)
print(bst.hasPathSum(T, 22))  # 1

T = TreeNode(5)
T.left = TreeNode(4)
T.left.left = TreeNode(-11)
T.right = TreeNode(8)
T.right.left = TreeNode(-13)
T.right.right = TreeNode(4)
print(bst.hasPathSum(T, -1))  # 0
