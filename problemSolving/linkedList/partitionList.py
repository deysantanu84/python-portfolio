# Given a linked list A and a value B, partition it such that
# all nodes less than B come before nodes greater than or equal to B.
# You should preserve the original relative order of the nodes in each of the two partitions.
# 1 <= |A| <= 10^6
# 1 <= A[i], B <= 10^9
# The first argument of input contains a pointer to the head to the given linked list.
# The second argument of input contains an integer, B.
# Return a pointer to the head of the modified linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def partition(self, A, B):
        lesser = ListNode("<")
        greaterEqual = ListNode(">=")

        temp1 = lesser
        temp2 = greaterEqual
        temp = A

        while temp:
            if temp.val < B:
                lesser.next = temp
                lesser = lesser.next

            else:
                greaterEqual.next = temp
                greaterEqual = greaterEqual.next

            temp = temp.next

        lesser.next = temp2.next
        greaterEqual.next = None

        return temp1.next


def printLinkedList(LL):
    tempNode = LL
    while tempNode:
        print(tempNode.val, end=' ')
        tempNode = tempNode.next
    print()


linkedList = Solution()
L = ListNode(1)
L1 = ListNode(4)
L2 = ListNode(3)
L3 = ListNode(2)
L4 = ListNode(5)
L5 = ListNode(2)
L.next = L1
L1.next = L2
L2.next = L3
L3.next = L4
L4.next = L5
printLinkedList(L)
printLinkedList(linkedList.partition(L, 3))  # [1, 2, 2, 4, 3, 5]

L = ListNode(1)
L1 = ListNode(2)
L2 = ListNode(3)
L3 = ListNode(1)
L4 = ListNode(3)
L.next = L1
L1.next = L2
L2.next = L3
L3.next = L4
printLinkedList(L)
printLinkedList(linkedList.partition(L, 2))  # [1, 1, 2, 3, 3]
