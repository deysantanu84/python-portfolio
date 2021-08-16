# Given an array of words A (dictionary) and another array B (which contain some words).
# You have to return the binary array (of length |B|) as the answer where 1 denotes that the word
# is present in the dictionary and 0 denotes it is not present.
# Formally, for each word in B, you need to return 1 if it is present in Dictionary and 0 if it is not.
# Such problems can be seen in real life when we work on any online editor (like Google Document),
# if the word is not valid it is underlined by a red line.
# NOTE: Try to do this in O(n) time complexity.
# 1 <= |A| <= 1000
# 1 <= sum of all strings in A <= 50000
# 1 <= |B| <= 1000
# First argument is array of strings A.
# First argument is array of strings B.
# Return the binary array of integers according to the given format.
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict()
        self.terminating = False


class Trie:
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()

    def getIndex(self, char):
        return ord(char) - ord('a')

    def insert(self, word):
        temp = self.root

        for i in range(len(word)):
            index = self.getIndex(word[i])

            if index not in temp.children:
                temp.children[index] = self.getNode()

            temp = temp.children.get(index)

        temp.terminating = True

    def search(self, word):
        temp = self.root

        for i in range(len(word)):
            index = self.getIndex(word[i])

            if not temp:
                return False

            temp = temp.children.get(index)

        if temp and temp.terminating:
            return True
        else:
            return False

    def delete(self, word):
        temp = self.root

        for i in range(len(word)):
            index = self.getIndex(word[i])
            if not temp:
                return 0

            temp = temp.children.get(index)

        if not temp:
            return 0
        else:
            temp.terminating = False
            return 1

    def update(self, oldWord, newWord):
        if self.delete(oldWord):
            self.insert(newWord)


class Solution:
    # @param A : list of strings
    # @param B : list of strings
    # @return a list of integers
    def solve(self, A, B):
        result = []
        node = Trie()

        for word in A:
            node.insert(word)

        for word in B:
            if node.search(word):
                result.append(1)
            else:
                result.append(0)

        return result


sol = Solution()
print(sol.solve(["hat", "cat", "rat"], ["cat", "ball"]))  # [1, 0]
print(sol.solve(["tape", "bcci"], ["table", "cci"]))  # [0, 0]
