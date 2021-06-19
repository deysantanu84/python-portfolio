# Given a linked list A, remove the B-th node from the end of list and return its head.
# For example, Given linked list: 1->2->3->4->5, and B = 2.
# After removing the second node from the end, the linked list becomes 1->2->3->5.
# NOTE: If B is greater than the size of the list, remove the first node of the list.
# NOTE: Try doing it using constant additional space.
# 1 <= |A| <= 10^6
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution:
	# @param A : head node of linked list
	# @param B : integer
	# @return the head node in the linked list
	def removeNthFromEnd(self, A, B):
		size = 0
		temp = A
		while temp.next:
			temp = temp.next
			size += 1

		if size < B:
			return A.next

		temp = temp2 = A

		for i in range(B):
			temp = temp.next

		if not temp:
			return A.next

		while temp.next:
			temp = temp.next
			temp2 = temp2.next

		temp2.next = temp2.next.next

		return A


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
printLinkedList(linkedList.removeNthFromEnd(L, 2))  # [1, 2, 3, 5]

L = ListNode(1)
printLinkedList(L)
printLinkedList(linkedList.removeNthFromEnd(L, 1))  # []
