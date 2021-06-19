# Given 3 array of integers A, B and C.
# A represents preorder traversal of a binary tree.
# B represents inorder traversal of a binary tree.
# C represents postorder traversal of a binary tree.
# Check whether these tree traversals are of the same tree or not.
# If they are of same tree return 1 else return 0.
# The arguments given are integer arrays A, B, and C.
# Return 1 if they are of same tree else return 0.
# 1 <= length of the array <= 1000
# all arrays are of same length
# 1 <= A[i], B[i], C[i] <= 10^9
class Solution:
    def checkTreeUtil(self, preorder, inorder, postorder, N):
        if N == 0:
            return 1

        if N == 1:
            if (preorder[0] == inorder[0]) and (inorder[0] == postorder[0]):
                return 1

        idx = -1

        for index in range(N):
            if inorder[index] == preorder[0]:
                idx = index
                break

        if idx == -1:
            return 0

        temp1 = self.checkTreeUtil(preorder[1:], inorder, postorder, idx)
        temp2 = self.checkTreeUtil(preorder[idx + 1:], inorder[idx + 1:], postorder[idx:], N - idx - 1)

        if temp1 and temp2:
            return 1
        else:
            return 0

    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        return self.checkTreeUtil(A, B, C, len(A))


binaryTree = Solution()
print(binaryTree.solve([1, 2, 4, 5, 3], [4, 2, 5, 1, 3], [4, 5, 2, 3, 1]))  # 1
print(binaryTree.solve([1, 5, 4, 2, 3], [4, 2, 5, 1, 3], [4, 1, 2, 3, 5]))  # 0
