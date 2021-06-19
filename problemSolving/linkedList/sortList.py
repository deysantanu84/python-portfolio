# Sort a linked list, A in O(n log n) time using constant space complexity.
# 0 <= |A| = 10^5
# The first and the only argument of input contains a pointer to the head of the linked list, A.
# Return a pointer to the head of the sorted linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution:
	def merge(self, list1, list2):
		temp = ListNode(-1)
		prev = temp

		while list1 and list2:
			if list1.val <= list2.val:
				prev.next = list1
				list1 = list1.next

			else:
				prev.next = list2
				list2 = list2.next

			prev = prev.next

		prev.next = list1 or list2

		return temp.next

	def mergeSort(self, A):
		if not A or not A.next:
			return A

		left = slow = fast = A
		fast = fast.next

		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next

		right = slow.next
		slow.next = None

		left_sorted = self.mergeSort(left)
		right_sorted = self.mergeSort(right)
		return self.merge(left_sorted, right_sorted)

	# @param A : head node of linked list
	# @return the head node in the linked list
	def sortList(self, A):
		return self.mergeSort(A)


def printLinkedList(LL):
	tempNode = LL
	while tempNode:
		print(tempNode.val, end=' ')
		tempNode = tempNode.next
	print()


linkedList = Solution()
L = ListNode(3)
L1 = ListNode(4)
L2 = ListNode(2)
L3 = ListNode(8)
L.next = L1
L1.next = L2
L2.next = L3
printLinkedList(L)
printLinkedList(linkedList.sortList(L))  # [2, 3, 4, 8]

L = ListNode(1)
printLinkedList(L)
printLinkedList(linkedList.sortList(L))  # [1]
