# You are given two linked lists, A and B representing two non-negative numbers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
# 1 <= |A|, |B| <= 10^5
# The first argument of input contains a pointer to the head of linked list A.
# The second argument of input contains a pointer to the head of linked list B.
# Return a pointer to the head of the required linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution:
	# @param A : head node of linked list
	# @param B : head node of linked list
	# @return the head node in the linked list
	def addTwoNumbers(self, A, B):
		curr = ListNode(0)
		temp = curr
		carry = 0

		while A or B or carry:
			if A:
				carry += A.val
				A = A.next

			if B:
				carry += B.val
				B = B.next

			curr.next = ListNode(carry % 10)
			curr = curr.next
			carry //= 10

		return temp.next


def printLinkedList(LL):
	tempNode = LL
	while tempNode:
		print(tempNode.val, end=' ')
		tempNode = tempNode.next
	print()


linkedList = Solution()
L = ListNode(2)
L1 = ListNode(4)
L2 = ListNode(3)
L.next = L1
L1.next = L2
printLinkedList(L)
M = ListNode(5)
M1 = ListNode(6)
M2 = ListNode(4)
M.next = M1
M1.next = M2
printLinkedList(M)
printLinkedList(linkedList.addTwoNumbers(L, M))  # [7, 0, 8]

L = ListNode(9)
L1 = ListNode(9)
L.next = L1
printLinkedList(L)
M = ListNode(1)
printLinkedList(M)
printLinkedList(linkedList.addTwoNumbers(L, M))  # [0, 0, 1]
