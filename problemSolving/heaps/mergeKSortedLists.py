# Given a list containing head pointers of N sorted linked lists.
# Merge these N given sorted linked lists and return it as one sorted list.
# 1 <= total number of elements in given linked lists <= 100000
# First and only argument is a list containing N head pointers.
# Return a pointer to the head of the sorted linked list after merging all the given linked lists.
from heapq import heappush, heappop


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):
        head = ListNode(None)
        temp = head
        heap = []
        for index in range(len(A)):
            if A[index]:
                heappush(heap, (A[index].val, index))
                A[index] = A[index].next

        while heap:
            val, i = heappop(heap)
            temp.next = ListNode(val)
            temp = temp.next

            if A[i]:
                heappush(heap, (A[i].val, i))
                A[i] = A[i].next

        return head.next


def printLinkedList(LL):
    tempNode = LL
    while tempNode:
        print(tempNode.val, end=' ')
        tempNode = tempNode.next
    print()


sol = Solution()
P = ListNode(1)
P.next = ListNode(10)
P.next.next = ListNode(20)
Q = ListNode(4)
Q.next = ListNode(11)
Q.next.next = ListNode(13)
R = ListNode(3)
R.next = ListNode(8)
R.next.next = ListNode(9)
printLinkedList(P)
printLinkedList(Q)
printLinkedList(R)
printLinkedList(sol.mergeKLists([P, Q, R]))  # 1 -> 3 -> 4 -> 8 -> 9 -> 10 -> 11 -> 13 -> 20

P = ListNode(10)
P.next = ListNode(12)
Q = ListNode(13)
R = ListNode(5)
R.next = ListNode(6)
printLinkedList(P)
printLinkedList(Q)
printLinkedList(R)
printLinkedList(sol.mergeKLists([P, Q, R]))  # 5 -> 6 -> 10 -> 12 -> 13
