# Given a binary tree, return a 2-D array with vertical order traversal of it.
# Go through the example and image for more details.
# NOTE: If 2 Tree Nodes shares the same vertical level then the one with lesser depth will come first.
# 0 <= number of nodes <= 10^5
# First and only argument is a pointer to the root node of binary tree, A.
# Return a 2D array denoting the vertical order traversal of tree as shown.
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

        result = []
        queue = [A]
        distDict = {A: 0}
        nodeDict = {0: [A.val]}
        minDist = 0
        maxDist = 0

        while len(queue):
            temp = queue.pop(0)

            if temp.left:
                queue.append(temp.left)
                distDict[temp.left] = distDict[temp] - 1
                dist = distDict[temp.left]
                if dist < minDist:
                    minDist = dist

                if dist not in nodeDict:
                    nodeDict[dist] = []
                nodeDict[dist].append(temp.left.val)

            if temp.right:
                queue.append(temp.right)
                distDict[temp.right] = distDict[temp] + 1
                dist = distDict[temp.right]
                if dist > maxDist:
                    maxDist = dist

                if dist not in nodeDict:
                    nodeDict[dist] = []
                nodeDict[dist].append(temp.right.val)

        for dist in range(minDist, maxDist + 1):
            result.append(nodeDict[dist])

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

T = TreeNode(8262)
T.right = TreeNode(411)
print(binaryTree.verticalOrderTraversal(T))  # [[8262], [411]]
