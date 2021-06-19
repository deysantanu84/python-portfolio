# Given a binary search tree of integers. You are given a range B and C.
# Return the count of the number of nodes that lies in the given range.
# 1 <= Number of nodes in binary tree <= 100000
# 0 <= B <= C <= 10^9
# First argument is a root node of the binary tree, A.
# Second argument is an integer B.
# Third argument is an integer C.
# Return the count of the number of nodes that lies in the given range.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        if not A:
            return 0

        if A.val == B and A.val == C:
            return 1

        if B <= A.val <= C:
            return 1 + self.solve(A.left, B, C) + self.solve(A.right, B, C)

        elif A.val < B:
            return self.solve(A.right, B, C)

        else:
            return self.solve(A.left, B, C)


bst = Solution()
T = TreeNode(15)
T.left = TreeNode(12)
T.left.left = TreeNode(10)
T.left.right = TreeNode(14)
T.left.left.left = TreeNode(8)
T.right = TreeNode(20)
T.right.left = TreeNode(16)
T.right.right = TreeNode(27)
print(bst.solve(T, 12, 20))  # 5

T = TreeNode(8)
T.left = TreeNode(6)
T.left.left = TreeNode(1)
T.left.right = TreeNode(4)
T.right = TreeNode(21)
print(bst.solve(T, 2, 20))  # 3
