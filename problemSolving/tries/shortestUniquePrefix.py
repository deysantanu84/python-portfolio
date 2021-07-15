# Given a list of N words. Find shortest unique prefix to represent each word in the list.
# NOTE: Assume that no word is prefix of another. In other words, the representation is always possible
# 1 <= Sum of length of all words <= 10^6
# First and only argument is a string array of size N.
# Return a string array B where B[i] denotes the shortest unique prefix to represent the ith word.
class TrieNode:
    def __init__(self):
        self.child = {}
        self.freq = 0
        self.ind = None


class Solution:
    def insert(self, root, word, ind):
        curr = root
        curr.ind = ind

        for char in word:
            curr.child.setdefault(char, TrieNode())
            curr.child[char].freq += 1
            curr.child[char].ind = ind
            curr = curr.child[char]

    def populateResult(self, root, curr, result):
        if not root:
            return

        if root.freq == 1:
            result.append((curr, root.ind))
            return

        for key, value in root.child.items():
            self.populateResult(value, curr + key, result)

        return result

    # @param A : list of strings
    # @return a list of strings
    def prefix(self, A):
        result = []
        root = TrieNode()

        for index in range(len(A)):
            self.insert(root, A[index], index)

        result = sorted(self.populateResult(root, "", result), key=lambda x: x[1])

        for i in range(len(result)):
            result[i] = result[i][0]

        return result


sol = Solution()
print(sol.prefix(["zebra", "dog", "duck", "dove"]))  # ["z", "dog", "du", "dov"]
print(sol.prefix(["apple", "ball", "cat"]))  # ["a", "b", "c"]
