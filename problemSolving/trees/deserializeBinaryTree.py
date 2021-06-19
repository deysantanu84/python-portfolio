# Given an integer array A denoting the Level Order Traversal of the Binary Tree.
# You have to Deserialize the given Traversal in the Binary Tree and return the root of the Binary Tree.
# NOTE:
# In the array, the NULL/None child is denoted by -1.
# For more clarification check the Example Input.
# 1 <= number of nodes <= 10^5
# -1 <= A[i] <= 10^5
# Only argument is an integer array A denoting the Level Order Traversal of the Binary Tree.
# Return the root node of the Binary Tree.
import sys
from collections import deque
sys.setrecursionlimit(10**6)


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : list of integers
    # @return the root node in the tree
    def solve(self, A):
        result = TreeNode(A[0])
        queue = deque([result])

        index = 1

        while queue:
            node = queue.pop()

            if index < len(A) and A[index] != -1:
                node.left = TreeNode(A[index])
                queue.appendleft(node.left)

            index += 1

            if index < len(A) and A[index] != -1:
                node.right = TreeNode(A[index])
                queue.appendleft(node.right)

            index += 1

        return result


def printTree(BT):
    if BT.left:
        printTree(BT.left)

    print(BT.val, end=' ')

    if BT.right:
        printTree(BT.right)


bt = Solution()
printTree(bt.solve([1, 2, 3, 4, 5, -1, -1, -1, -1, -1, -1]))  # 4 2 5 1 3
print()
printTree(bt.solve([1, 2, 3, 4, 5, -1, 6, -1, -1, -1, -1, -1, -1]))  # 4 2 5 1 3 6
