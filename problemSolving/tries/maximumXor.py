# Given an array of integers A, find and return the maximum result of A[i] XOR A[j],
# where i, j are the indexes of the array.
# 1 <= length of the array <= 100000
# 0 <= A[i] <= 10^9
# The only argument given is the integer array A.
# Return an integer denoting the maximum result of A[i] XOR A[j].
class TrieNode:
    def __init__(self):
        self.children = {}
        self.val = 0


class Trie:
    def __init__(self, n):
        self.root = TrieNode()
        self.n = n

    def add_num(self, num):
        node = self.root

        for shift in range(self.n, -1, -1):
            if num & (1 << shift):
                val = 1
            else:
                val = 0

            if val not in node.children:
                node.children[val] = TrieNode()

            node = node.children[val]

        node.val = num


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        maxLength = len(bin(max(A))) - 2
        trie = Trie(maxLength)

        for item in A:
            trie.add_num(item)

        result = 0

        for item in A:
            node = trie.root

            for bitCount in range(maxLength, -1, -1):
                if item & (1 << bitCount):
                    val = 1
                else:
                    val = 0

                if 1 - val in node.children:
                    node = node.children[1 - val]
                else:
                    node = node.children[val]

            result = max(result, item ^ node.val)

        return result


maxXor = Solution()
print(maxXor.solve([1, 2, 3, 4, 5]))  # 7
print(maxXor.solve([5, 17, 100, 11]))  # 117
