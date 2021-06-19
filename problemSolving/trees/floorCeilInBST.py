# Given a Binary Search Tree rooted at A.
# Given an integer array B of size N. Find the floor and ceil of every element of the array B.
# Floor(X) is the highest element in the tree <= X, while the ceil(X) is the lowest element in the tree >= X.
# NOTE: If floor or ceil of any element of B doesn't exists, output -1 for the value which doesn't exists.
# 0 <= Number of nodes in the tree <= 1000000
# 0 <= node values <= 10^9
# 0 <= N <= 100000
# 0 <= B[i] <= 10^9
# First argument represents the root of binary tree A.
# Second argument is an integer array B.
# Return an integer array C of size N*2. C[i][0] denotes the floor value of B[i] and C[i][1]
# represents the ceil value of B[i] in the given tree.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def floorCeilBSTUtil(self, A, elem):
        floor = -1
        ceil = -1

        while A:
            if A.val == elem:
                return [A.val, A.val]

            elif elem > A.val:
                floor = A.val
                A = A.right

            else:
                ceil = A.val
                A = A.left

        return [floor, ceil]

    # @param A : root node of tree
    # @param B : list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        result = []

        for item in B:
            result.append(self.floorCeilBSTUtil(A, item))

        return result


bst = Solution()
T = TreeNode(10)
T.left = TreeNode(4)
T.left.left = TreeNode(1)
T.left.right = TreeNode(8)
T.right = TreeNode(15)
print(bst.solve(T, [4, 19]))  # [[4, 4], [15, -1]]

T = TreeNode(8)
T.left = TreeNode(5)
T.left.left = TreeNode(4)
T.left.right = TreeNode(7)
T.right = TreeNode(19)
T.right.right = TreeNode(100)
print(bst.solve(T, [1, 11]))  # [[-1, 4], [8, 19]]

# 32 25 46 17 27 40 49 9 -1 -1 -1 -1 -1 -1 -1 -1 -1
T = TreeNode(32)
T.left = TreeNode(25)
T.left.left = TreeNode(17)
T.left.left.left = TreeNode(9)
T.left.right = TreeNode(27)
T.right = TreeNode(46)
T.right.left = TreeNode(40)
T.right.right = TreeNode(49)
print(bst.solve(T, [5, 9, 5, 15, 7]))  # [[-1, 9], [9, 9], [-1, 9], [9, 17], [-1, 9]]
