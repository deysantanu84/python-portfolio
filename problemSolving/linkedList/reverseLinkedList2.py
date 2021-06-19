# Reverse a linked list A from position B to C.
# NOTE: Do it in-place and in one-pass.
# 1 <= |A| <= 10^6
# 1 <= B <= C <= |A|
# The first argument contains a pointer to the head of the given linked list, A.
# The second argument contains an integer, B.
# The third argument contains an integer C.
# Return a pointer to the head of the modified linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution:
	# @param A : head node of linked list
	# @param B : integer
	# @param C : integer
	# @return the head node in the linked list
	def reverseBetween(self, A, B, C):
		if not A:
			return A

		temp = A
		prev = None

		for _ in range(B - 1):
			prev = temp
			temp = temp.next

		tail = temp
		temp2 = prev

		for _ in range(C - B + 1):
			third = temp.next
			temp.next = prev
			prev = temp
			temp = third

		if temp2:
			temp2.next = prev
		else:
			A = prev

		tail.next = temp

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
printLinkedList(linkedList.reverseBetween(L, 2, 4))  # 1 -> 4 -> 3 -> 2 -> 5

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
printLinkedList(linkedList.reverseBetween(L, 1, 5))  # 5 -> 4 -> 3 -> 2 -> 1
