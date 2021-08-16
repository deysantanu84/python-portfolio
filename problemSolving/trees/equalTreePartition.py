# Given a binary tree A. Check whether it is possible to partition the tree to two trees which have
# equal sum of values after removing exactly one edge on the original tree.
# 1 <= size of tree <= 100000
# -10^9 <= value of node <= 10^9
# First and only argument is head of tree A.
# Return 1 if the tree can be partitioned into two trees of equal sum else return 0.
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    flag = False

    def treeSum(self, root):
        if not root:
            return 0
        return root.val + self.treeSum(root.left) + self.treeSum(root.right)

    def checkSum(self, root, targetSum, origRoot):
        if not root:
            return 0

        leftSum = self.checkSum(root.left, targetSum, origRoot)
        rightSum = self.checkSum(root.right, targetSum, origRoot)
        tempSum = root.val + leftSum + rightSum

        if tempSum == targetSum and root != origRoot:
            Solution.flag = True
            return tempSum

        return tempSum

    # @param A : root node of tree
    # @return an integer
    def solve(self, A):
        if Solution.flag:
            Solution.flag = False

        tempSum = self.treeSum(A)
        if tempSum:
            tempSum //= 2

        self.checkSum(A, tempSum, A)
        if Solution.flag:
            return 1

        return 0


sol = Solution()
T = TreeNode(5)
T.left = TreeNode(3)
T.left.left = TreeNode(4)
T.left.right = TreeNode(6)
T.right = TreeNode(7)
T.right.left = TreeNode(5)
T.right.right = TreeNode(6)
print(sol.solve(T))  # 1

T = TreeNode(1)
T.left = TreeNode(2)
T.right = TreeNode(10)
T.right.left = TreeNode(20)
T.right.right = TreeNode(2)
print(sol.solve(T))  # 0
