# Given a linked list of integers. Find and return the middle element of the linked list.
# NOTE: If there are N nodes in the linked list and N is even then return the (N/2 + 1)th element.
# 1 <= length of the linked list <= 100000
# 1 <= Node value <= 10^9
# The only argument given head pointer of linked list.
# Return the middle element of the linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @return an integer
    def solve(self, A):
        temp1 = A
        temp2 = A

        while temp2 and temp2.next:
            temp1 = temp1.next
            temp2 = temp2.next.next

        return temp1.val


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
L.next = L1
L1.next = L2
L2.next = L3
L3.next = L4
printLinkedList(L)
print(linkedList.solve(L))  # 3

L = ListNode(1)
L1 = ListNode(5)
L2 = ListNode(6)
L3 = ListNode(2)
L4 = ListNode(3)
L5 = ListNode(4)
L.next = L1
L1.next = L2
L2.next = L3
L3.next = L4
L4.next = L5
printLinkedList(L)
print(linkedList.solve(L))  # 2
