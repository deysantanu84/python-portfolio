# Given an array of integers A. Find and return the number of subarrays whose xor values is less than B.
# NOTE: As the answer can be very large, return the answer modulo (10^9+7).
# 1 <= length of the array <= 100000
# 1 <= A[i] <= 10^5
# 1 <= B <= 10^6
# The argument given is the integer array A
# Second argument is an integer B.
# Return an integer denoting the number of subarrays whose xor values is less than B.
class TrieNode:
    def __init__(self):
        self.val = 0
        self.left = None
        self.right = None


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.result = 0

    def insert(self, value):
        temp = self.root
        value = '{:032b}'.format(value)

        for char in value:
            if char == '1':
                if not temp.right:
                    temp.right = TrieNode()

                temp = temp.right

            else:
                if not temp.left:
                    temp.left = TrieNode()

                temp = temp.left

            temp.val += 1

    def query(self, prefix, B):
        temp = self.root
        prefix = '{:032b}'.format(prefix)
        B = '{:032b}'.format(B)

        for index in range(32):
            if prefix[index] == '1':
                if B[index] == '1':
                    if temp.right:
                        self.result += temp.right.val

                    if temp.left:
                        temp = temp.left

                    else:
                        break

                else:
                    if temp.right:
                        temp = temp.right

                    else:
                        break

            else:
                if B[index] == '1':
                    if temp.left:
                        self.result += temp.left.val

                    if temp.right:
                        temp = temp.right

                    else:
                        break

                else:
                    if temp.left:
                        temp = temp.left

                    else:
                        break


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        node = Trie()
        node.insert(0)
        prefix = 0

        for item in A:
            prefix ^= item
            node.query(prefix, B)
            node.insert(prefix)

        return node.result % (10 ** 9 + 7)


sol = Solution()
print(sol.solve([8, 3, 10, 2, 6, 7, 6, 9, 3], 3))  # 5
print(sol.solve([9, 4, 3, 11], 7))  # 3
