# Given a linked list of integers.
# Find and return the length of the longest palindrome list that exists in that linked list.
# A palindrome list is a list that reads the same backward and forward.
# Expected memory complexity : O(1)
# 1 <= length of the linked list <= 2000
# 1 <= Node value <= 100
# The only argument given is head pointer of the linked list.
# Return the length of the longest palindrome list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def countUtil(self, x, y):
        count = 0

        while x and y:
            if x.val != y.val:
                break
            else:
                count += 1

            x = x.next
            y = y.next

        return count

    # @param A : head node of linked list
    # @return an integer
    def solve(self, A):
        result = 0
        prev = None
        temp = A

        while temp:
            next = temp.next
            temp.next = prev

            result = max(result, 2 * self.countUtil(prev, next) + 1)
            result = max(result, 2 * self.countUtil(temp, next))

            prev = temp
            temp = next

        return result


def printLinkedList(LL):
    tempNode = LL
    while tempNode:
        print(tempNode.val, end=' ')
        tempNode = tempNode.next
    print()


linkedList = Solution()
L = ListNode(2)
L1 = ListNode(3)
L2 = ListNode(3)
L3 = ListNode(3)
L.next = L1
L1.next = L2
L2.next = L3
printLinkedList(L)
print(linkedList.solve(L))  # 3

L = ListNode(2)
L1 = ListNode(1)
L2 = ListNode(2)
L3 = ListNode(1)
L4 = ListNode(2)
L5 = ListNode(2)
L6 = ListNode(1)
L7 = ListNode(3)
L8 = ListNode(2)
L9 = ListNode(2)
L.next = L1
L1.next = L2
L2.next = L3
L3.next = L4
L4.next = L5
L5.next = L6
L6.next = L7
L7.next = L8
L8.next = L9
printLinkedList(L)
print(linkedList.solve(L))  # 5
