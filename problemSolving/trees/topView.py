# Given a binary tree of integers denoted by root A.
# Return an array of integers representing the top view of the Binary tree.
# Top view of a Binary Tree is a set of nodes visible when the tree is visited from top.
# Return the nodes in any order.
# 1 <= Number of nodes in binary tree <= 100000
# 0 <= node values <= 10^9
# First and only argument is head of the binary tree A.
# Return an array, representing the top view of the binary tree.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, A):
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

        result = []
        for nodeList in nodeMap.values():
            result.append(nodeList[0])

        return result


binaryTree = Solution()
T = TreeNode(1)
T.left = TreeNode(2)
T.left.left = TreeNode(4)
T.left.left.left = TreeNode(8)
T.left.right = TreeNode(5)
T.right = TreeNode(3)
T.right.left = TreeNode(6)
T.right.right = TreeNode(7)
print(binaryTree.solve(T))  # [1, 2, 4, 8, 3, 7]

T = TreeNode(1)
T.left = TreeNode(2)
T.left.right = TreeNode(4)
T.left.right.right = TreeNode(5)
T.right = TreeNode(3)
print(binaryTree.solve(T))  # [1, 2, 3]
