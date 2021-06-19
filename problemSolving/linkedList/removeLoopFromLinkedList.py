# Given a linked list which contains some loop.
# You need to find the node, which creates a loop, and break it by making the node point to NULL.
# 1 <= number of nodes <= 1000
# Only argument is the head of the linked list.
# Return the head of the updated linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution:
	def removeLoop(self, A, node):
		temp1 = A
		while True:
			temp2 = node

			while temp2.next != node and temp2.next != temp1:
				temp2 = temp2.next

			if temp2.next == temp1:
				break

			temp1 = temp1.next

		temp2.next = None

	# @param A : head node of linked list
	# @return the head node in the linked list
	def solve(self, A):
		slow = A
		fast = A

		while slow and fast and fast.next:
			slow = slow.next
			fast = fast.next.next

			if slow == fast:
				self.removeLoop(A, slow)

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
L.next = L1
L1.next = L
printLinkedList(linkedList.solve(L))  # 1 -> 2 -> NULL

L = ListNode(3)
L1 = ListNode(2)
L2 = ListNode(4)
L3 = ListNode(5)
L4 = ListNode(6)
L.next = L1
L1.next = L2
L2.next = L3
L3.next = L4
L4.next = L2
printLinkedList(linkedList.solve(L))  # 3 -> 2 -> 4 -> 5 -> 6 -> NULL
