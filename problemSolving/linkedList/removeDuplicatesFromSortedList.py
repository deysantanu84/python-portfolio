# Given a sorted linked list, delete all duplicates such that each element appear only once.
# 0 <= length of linked list <= 10^6
# First argument is the head pointer of the linked list.
# Return the head pointer of the linked list after removing all duplicates.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def deleteDuplicates(self, A):
		temp = A

		while temp:
			while temp.next and temp.next.val == temp.val:
				temp.next = temp.next.next

			temp = temp.next

		return A


def printLinkedList(LL):
	tempNode = LL
	while tempNode:
		print(tempNode.val, end=' ')
		tempNode = tempNode.next
	print()


linkedList = Solution()
L = ListNode(1)
L1 = ListNode(1)
L2 = ListNode(2)
L.next = L1
L1.next = L2
printLinkedList(L)
printLinkedList(linkedList.deleteDuplicates(L))  # 1->2

linkedList = Solution()
L = ListNode(1)
L1 = ListNode(1)
L2 = ListNode(2)
L3 = ListNode(3)
L4 = ListNode(3)
L.next = L1
L1.next = L2
L2.next = L3
L3.next = L4
printLinkedList(L)
printLinkedList(linkedList.deleteDuplicates(L))  # 1->2->3
