# Merge two sorted linked lists A and B and return it as a new list.
# The new list should be made by splicing together the nodes of the first two lists,
# and should also be sorted.
# 0 <= |A|, |B| <= 10^5
# The first argument of input contains a pointer to the head of linked list A.
# The second argument of input contains a pointer to the head of linked list B.
# Return a pointer to the head of the merged linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution:
	# @param A : head node of linked list
	# @param B : head node of linked list
	# @return the head node in the linked list
	def mergeTwoLists(self, A, B):
		head = sortedList = ListNode(0)

		while A and B:
			if A.val < B.val:
				sortedList.next = A
				A = A.next
				sortedList = sortedList.next

			elif A.val >= B.val:
				sortedList.next = B
				B = B.next
				sortedList = sortedList.next

		sortedList.next = A or B

		return head.next


def printLinkedList(LL):
	tempNode = LL
	while tempNode:
		print(tempNode.val, end=' ')
		tempNode = tempNode.next
	print()


linkedList = Solution()
L = ListNode(5)
L1 = ListNode(8)
L2 = ListNode(20)
L.next = L1
L1.next = L2
printLinkedList(L)
M = ListNode(4)
M1 = ListNode(11)
M2 = ListNode(15)
M.next = M1
M1.next = M2
printLinkedList(M)
printLinkedList(linkedList.mergeTwoLists(L, M))  # 4 -> 5 -> 8 -> 11 -> 15 -> 20

L = ListNode(1)
L1 = ListNode(2)
L2 = ListNode(3)
L.next = L1
L1.next = L2
printLinkedList(L)
printLinkedList(linkedList.mergeTwoLists(L, None))  # 1 -> 2 -> 3
