# Two elements of a binary search tree (BST),represented by root A are swapped by mistake.
# Tell us the 2 values swapping which the tree will be restored.
# A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?
# 1 <= size of tree <= 100000
# First and only argument is the head of the tree,A
# Return the 2 elements which need to be swapped.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.first = None
        self.second = None
        self.previous = None

    def traverse(self, root):
        if not root:
            return

        self.traverse(root.left)

        if self.previous:
            if self.previous.val > root.val:
                if not self.first:
                    self.first = self.previous

                self.second = root

        self.previous = root

        self.traverse(root.right)

    # @param A : root node of tree
    # @return a list of integers
    def recoverTree(self, A):
        self.traverse(A)
        return [self.second.val, self.first.val]


bst = Solution()
T = TreeNode(1)
T.left = TreeNode(2)
T.right = TreeNode(3)
print(bst.recoverTree(T))  # [1, 2]

bst = Solution()
T = TreeNode(2)
T.left = TreeNode(3)
T.right = TreeNode(1)
print(bst.recoverTree(T))  # [1, 3]
