# Find the lowest common ancestor in an unordered binary tree A given two values B and C in the tree.
# Lowest common ancestor : the lowest common ancestor (LCA) of two nodes v and w in a tree or
# directed acyclic graph (DAG) is the lowest (i.e. deepest) node that has both v and w as descendants.
# 1 <= size of tree <= 100000
# 1 <= B, C <= 10^9
# First argument is head of tree A.
# Second argument is integer B.
# Third argument is integer C.
# Return the LCA.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lcaUtil(self, P, Q, R):
        if not P:
            return False, False, None

        leftContainsQ, leftContainsR, leftContainsResult = self.lcaUtil(P.left, Q, R)
        rightContainsQ, rightContainsR, rightContainsResult = self.lcaUtil(P.right, Q, R)

        isParentOfQ = leftContainsQ or rightContainsQ or P.val == Q
        isParentOfR = leftContainsR or rightContainsR or P.val == R

        if isParentOfQ and isParentOfR:
            result = P
        else:
            result = None

        result = leftContainsResult or rightContainsResult or result

        return isParentOfQ, isParentOfR, result

    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    def lca(self, A, B, C):
        _, _, result = self.lcaUtil(A, B, C)

        if result:
            return result.val
        else:
            return -1


tree = Solution()
T = TreeNode(1)
T.left = TreeNode(2)
T.right = TreeNode(3)
print(tree.lca(T, 2, 3))  # 1

T = TreeNode(1)
T.left = TreeNode(2)
T.left.left = TreeNode(4)
T.left.right = TreeNode(5)
T.right = TreeNode(3)
print(tree.lca(T, 4, 5))  # 2

T = TreeNode(4)
T.left = TreeNode(8)
T.left.left = TreeNode(13)
T.left.right = TreeNode(6)
T.left.right.left = TreeNode(9)
T.left.right.left.left = TreeNode(12)
T.left.right.right = TreeNode(10)
T.left.right.right.left = TreeNode(2)
T.left.right.right.right = TreeNode(11)
T.left.right.right.right.right = TreeNode(5)
T.left.right.right.right.right.left = TreeNode(1)
T.left.right.right.right.right.left.right = TreeNode(3)
T.right = TreeNode(7)
print(tree.lca(T, 31, 39))  # -1

T = TreeNode(16)
T.left = TreeNode(23)
T.left.right = TreeNode(1)
T.left.right.left = TreeNode(25)
T.left.right.left.left = TreeNode(14)
T.left.right.left.left.right = TreeNode(3)
T.left.right.left.left.right.left = TreeNode(10)
T.left.right.left.left.right.left.right = TreeNode(20)
T.left.right.right = TreeNode(19)
T.left.right.right.left = TreeNode(30)
T.left.right.right.left.right = TreeNode(8)
T.left.right.right.left.right.left = TreeNode(5)
T.left.right.right.right = TreeNode(4)
T.right = TreeNode(9)
T.right.left = TreeNode(22)
T.right.left.left = TreeNode(6)
T.right.left.left.left = TreeNode(26)
T.right.left.left.left.left = TreeNode(12)
T.right.left.left.left.left.left = TreeNode(17)
T.right.left.left.left.left.right = TreeNode(11)
T.right.left.left.left.left.right.right = TreeNode(15)
T.right.left.left.left.left.right.right.right = TreeNode(27)
T.right.left.left.left.right = TreeNode(18)
T.right.left.left.left.right.left = TreeNode(21)
T.right.left.left.left.right.right = TreeNode(7)
T.right.left.left.right = TreeNode(29)
T.right.left.left.right.left = TreeNode(28)
T.right.left.right = TreeNode(13)
T.right.right = TreeNode(2)
T.right.right.right = TreeNode(24)
print(tree.lca(T, 32, 24))  # -1
