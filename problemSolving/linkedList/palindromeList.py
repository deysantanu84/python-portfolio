# Given a singly linked list A, determine if its a palindrome.
# Return 1 or 0 denoting if its a palindrome or not, respectively.
# 1 <= |A| <= 10^5
# The first and the only argument of input contains a pointer to the head of the given linked list.
# Return 0, if the linked list is not a palindrome.
# Return 1, if the linked list is a palindrome.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution:
	# @param A : head node of linked list
	# @return an integer
	def isPalindrome(self, A):
		if not A or not A.next:
			return 1

		temp1 = A
		temp2 = A
		reversedList = None

		while temp2 is not None and temp2.next is not None:
			temp = temp1

			temp1 = temp1.next
			temp2 = temp2.next.next

			temp.next = reversedList
			reversedList = temp

		if temp2 is not None:
			temp1 = temp1.next

		while reversedList is not None and reversedList.val == temp1.val:
			reversedList = reversedList.next
			temp1 = temp1.next

		if reversedList is None:
			return 1
		else:
			return 0


def printLinkedList(LL):
	tempNode = LL
	while tempNode:
		print(tempNode.val, end=' ')
		tempNode = tempNode.next
	print()


linkedList = Solution()
L = ListNode(1)
L1 = ListNode(2)
L2 = ListNode(2)
L3 = ListNode(1)
L.next = L1
L1.next = L2
L2.next = L3
printLinkedList(L)
print(linkedList.isPalindrome(L))  # 1

L = ListNode(1)
L1 = ListNode(3)
L2 = ListNode(2)
L.next = L1
L1.next = L2
printLinkedList(L)
print(linkedList.isPalindrome(L))  # 0
