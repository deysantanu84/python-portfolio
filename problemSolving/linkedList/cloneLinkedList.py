# Given a doubly linked list of integers with one pointer of each node
# pointing to the next node (just like in a single link list) while the second pointer,
# however, can point to any node in the list and not just the previous node.
# You have to create a copy of this list and return the head pointer of the duplicated list.
# 1 <= length of the list <= 100000
# 1 <= Value of node <= 100000
# The only argument given is head pointer of the doubly linked list.
# Return the head pointer of the duplicated list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None
		self.random = None


def clonelist(A):
	cloneDict = {}
	temp = A

	while temp:
		cloneDict[temp] = ListNode(temp.val)
		temp = temp.next

	temp = A

	while temp:
		if temp.next:
			cloneDict[temp].next = cloneDict[temp.next]

		if temp.random:
			cloneDict[temp].random = cloneDict[temp.random]

		temp = temp.next

	return cloneDict[A]


def printLinkedList(LL):
	tempNode = LL
	while tempNode:
		print(tempNode.val, end='->')
		tempNode = tempNode.next
	print()

	tempNode = LL
	while tempNode:
		print(tempNode.val, end='->')
		print(tempNode.random.val, end=' ')
		tempNode = tempNode.next
	print()


L = ListNode(1)
L1 = ListNode(2)
L2 = ListNode(3)
L3 = ListNode(4)
L4 = ListNode(5)
L.next = L1
L.random = L4
L1.next = L2
L1.random = L3
L2.next = L3
L2.random = L2
L3.next = L4
L3.random = L1
L4.random = L
printLinkedList(L)
printLinkedList(clonelist(L))
