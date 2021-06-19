# Given a singly linked list A and an integer B,
# reverse the nodes of the list B at a time and return modified linked list.
# 1 <= |A| <= 10^3
# B always divides A
# The first argument of input contains a pointer to the head of the linked list.
# The second argument of input contains the integer, B.
# Return a pointer to the head of the modified linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseListUtil(self, A, B, remainingNodes):
        if remainingNodes < B:
            return A

        count = 0
        prev = None
        next = None
        current = A

        while current and count < B:
            count += 1
            remainingNodes -= 1
            next = current.next
            current.next = prev
            prev = current
            current = next

        if next:
            A.next = self.reverseListUtil(next, B, remainingNodes)

        return prev

    def kReverseLinkedList(self, A, B):
        remainingNodes = 0
        temp = A

        while temp:
            remainingNodes += 1
            temp = temp.next

        return self.reverseListUtil(A, B, remainingNodes)


def printLinkedList(LL):
    tempNode = LL
    while tempNode:
        print(tempNode.val, end=' ')
        tempNode = tempNode.next
    print()


linkedList = Solution()
L = ListNode(1)
L1 = ListNode(2)
L2 = ListNode(3)
L3 = ListNode(4)
L4 = ListNode(5)
L5 = ListNode(6)
L.next = L1
L1.next = L2
L2.next = L3
L3.next = L4
L4.next = L5
printLinkedList(L)
printLinkedList(linkedList.kReverseLinkedList(L, 2))  # [2, 1, 4, 3, 6, 5]

L = ListNode(1)
L1 = ListNode(2)
L2 = ListNode(3)
L3 = ListNode(4)
L4 = ListNode(5)
L5 = ListNode(6)
L.next = L1
L1.next = L2
L2.next = L3
L3.next = L4
L4.next = L5
printLinkedList(L)
printLinkedList(linkedList.kReverseLinkedList(L, 3))  # [3, 2, 1, 6, 5, 4]
