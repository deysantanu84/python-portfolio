# Given a singly linked list A
#  A: A0 → A1 → … → An-1 → An
# reorder it to:
#  A0 → An → A1 → An-1 → A2 → An-2 → …
# You must do this in-place without altering the nodes' values.
# 1 <= |A| <= 10^6
# The first and the only argument of input contains a pointer to the head of the linked list A.
# Return a pointer to the head of the modified linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def reorderList(self, A):
		array = []
		temp = A
		size = 0

		while temp:
			array.append(temp)
			temp = temp.next
			size += 1

		start = 0
		end = size - 1
		last = A

		while start < end:
			array[start].next = array[end]
			start += 1

			if start == end:
				last = array[end]
				break

			array[end].next = array[start]
			end -= 1
			last = array[start]

		if last:
			last.next = None

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
linkedList.reorderList(L)  # [1, 5, 2, 4, 3]
printLinkedList(L)

L = ListNode(1)
L1 = ListNode(2)
L2 = ListNode(3)
L3 = ListNode(4)
L.next = L1
L1.next = L2
L2.next = L3
printLinkedList(L)
linkedList.reorderList(L)  # [1, 4, 2, 3]
printLinkedList(L)

L = ListNode(1)
printLinkedList(L)
linkedList.reorderList(L)  # [1]
printLinkedList(L)

L = ListNode(1)
L1 = ListNode(2)
L.next = L1
printLinkedList(L)
linkedList.reorderList(L)  # [2, 1]
printLinkedList(L)
