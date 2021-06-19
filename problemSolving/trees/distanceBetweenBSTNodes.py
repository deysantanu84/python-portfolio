# Given a binary search tree.
# Return the distance between two nodes with given two keys B and C.
# It may be assumed that both keys exist in BST.
# NOTE: Distance between two nodes is number of edges between them.
# 1 <= Number of nodes in binary tree <= 1000000
# 0 <= node values <= 10^9
# First argument is a root node of the binary tree, A.
# Second argument is an integer B.
# Third argument is an integer C.
# Return an integer denoting the distance between two nodes with given two keys B and C
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathToNode(self, A, path, value):
        if not A:
            return False

        path.append(A.val)

        if A.val == value:
            return True

        if ((A.left and self.pathToNode(A.left, path, value)) or
                (A.right and self.pathToNode(A.right, path, value))):
            return True

        path.pop()

        return False

    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        if A:
            pathB = []
            self.pathToNode(A, pathB, B)

            pathC = []
            self.pathToNode(A, pathC, C)

            index = 0
            while index < len(pathB) and index < len(pathC):
                if pathB[index] != pathC[index]:
                    break
                index += 1

            return len(pathB) + len(pathC) - 2*index

        else:
            return 0


bst = Solution()
T = TreeNode(5)
T.left = TreeNode(2)
T.left.left = TreeNode(1)
T.left.right = TreeNode(4)
T.right = TreeNode(8)
T.right.left = TreeNode(6)
T.right.right = TreeNode(11)
print(bst.solve(T, 2, 11))  # 3

T = TreeNode(6)
T.left = TreeNode(2)
T.left.left = TreeNode(1)
T.left.right = TreeNode(4)
T.right = TreeNode(9)
T.right.left = TreeNode(7)
T.right.right = TreeNode(10)
print(bst.solve(T, 2, 6))  # 1
