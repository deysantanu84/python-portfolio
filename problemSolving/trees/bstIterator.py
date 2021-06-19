# Implement an iterator over a binary search tree (BST).
# Your iterator will be initialized with the root node of a BST.
# The first call to next() will return the smallest number in BST.
# Calling next() again will return the next smallest number in the BST, and so on.
# Note: next() and hasNext() should run in average O(1) time and uses O(h) memory,
# where h is the height of the tree. Try to optimize the additional
# space complexity apart from the amortized time complexity.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator:
    stack = []

    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.pushLeft(root)

    def pushLeft(self, node):
        if node:
            self.stack.append(node)
            self.pushLeft(node.left)

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        if len(self.stack) > 0:
            return True

        return False

    # @return an integer, the next smallest number
    def next(self):
        item = self.stack.pop()

        self.pushLeft(item.right)

        return item.val


# Your BSTIterator will be called like this:
# i = BSTIterator(root)
# while i.hasNext(): print i.next(),
