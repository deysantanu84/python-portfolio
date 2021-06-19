# Given a binary tree
#     struct TreeLinkNode {
#       TreeLinkNode *left;
#       TreeLinkNode *right;
#       TreeLinkNode *next;
#     }
# Populate each next pointer to point to its next right node.
# If there is no next right node, the next pointer should be set to NULL.
# Initially, all next pointers are set to NULL.
# Note:
# You may only use constant extra space.
# Note 1: that using recursion has memory overhead and does not qualify for constant space.
# Note 2: The tree need not be a perfect binary tree.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if not root:
            return

        current = root
        firstInRow = None
        previous = None

        while current:
            while current:
                if current.left:
                    if not previous:
                        firstInRow = current.left

                    else:
                        previous.next = current.left

                    previous = current.left

                if current.right:
                    if not previous:
                        firstInRow = current.right

                    else:
                        previous.next = current.right

                    previous = current.right

                current = current.next

            current = firstInRow
            previous = firstInRow = None
