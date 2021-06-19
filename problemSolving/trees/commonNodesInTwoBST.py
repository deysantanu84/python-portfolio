# Given two BSTs A and B, return the (sum of all common nodes in both A and B) % (10^9 +7) .
# In case there is no common node, return 0.
# NOTE:
# Try to do it one pass through the trees.
# 1 <= Number of nodes in the tree A and B <= 10^5
# 1 <= Node values <= 10^6
# First argument represents the root of BST A.
# Second argument represents the root of BST B.
# Return an integer denoting the (sum of all common nodes in both BSTs A and B) % (10^9 +7) .
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @param B : root node of tree
    # @return an integer
    def solve(self, A, B):
        result = 0
        tempA = A
        tempB = B
        stackA = []
        stackB = []

        while 1:
            if tempA:
                stackA.append(tempA)
                tempA = tempA.left

            elif tempB:
                stackB.append(tempB)
                tempB = tempB.left

            elif len(stackA) and len(stackB):
                tempA = stackA[-1]
                tempB = stackB[-1]

                if tempA.val == tempB.val:
                    result += tempA.val
                    stackA.pop()
                    stackB.pop()

                    tempA = tempA.right
                    tempB = tempB.right

                elif tempA.val < tempB.val:
                    stackA.pop()
                    tempA = tempA.right
                    tempB = None

                elif tempA.val > tempB.val:
                    stackB.pop()
                    tempB = tempB.right
                    tempA = None

            else:
                break

        return result % (10**9 + 7)


bst = Solution()
P = TreeNode(5)
P.left = TreeNode(2)
P.left.right = TreeNode(3)
P.right = TreeNode(8)
P.right.right = TreeNode(15)
P.right.right.left = TreeNode(9)
Q = TreeNode(7)
Q.left = TreeNode(1)
Q.left.right = TreeNode(2)
Q.right = TreeNode(10)
Q.right.right = TreeNode(15)
Q.right.right.left = TreeNode(11)
print(bst.solve(P, Q))  # 17

P = TreeNode(7)
P.left = TreeNode(1)
P.left.right = TreeNode(2)
P.right = TreeNode(10)
P.right.right = TreeNode(15)
P.right.right.left = TreeNode(11)
Q = TreeNode(7)
Q.left = TreeNode(1)
Q.left.right = TreeNode(2)
Q.right = TreeNode(10)
Q.right.right = TreeNode(15)
Q.right.right.left = TreeNode(11)
print(bst.solve(P, Q))  # 46
