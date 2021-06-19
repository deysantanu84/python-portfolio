# Given a linked list A, swap every two adjacent nodes and return its head.
# NOTE: Your algorithm should use only constant space.
# You may not modify the values in the list, only nodes itself can be changed.
# 1 <= |A| <= 10^6
# The first and the only argument of input contains a pointer to the head of the given linked list.
# Return a pointer to the head of the modified linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def swapPairs(self, A):
		temp = ListNode(0)
		prev = temp
		prev.next = A

		while prev.next and prev.next.next:
			p = prev.next
			q = prev.next.next
			r = prev.next.next.next

			prev.next = q
			prev.next.next = p
			prev.next.next.next = r
			prev = prev.next.next

		return temp.next


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
L.next = L1
L1.next = L2
L2.next = L3
printLinkedList(L)
printLinkedList(linkedList.swapPairs(L))  # 2 -> 1 -> 4 -> 3

L = ListNode(7)
L1 = ListNode(2)
L2 = ListNode(1)
L.next = L1
L1.next = L2
printLinkedList(L)
printLinkedList(linkedList.swapPairs(L))  # 2 -> 7 -> 1
