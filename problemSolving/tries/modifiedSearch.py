# Given two arrays of strings A of size N and B of size M.
# Return a binary string C where C[i] = '1' if B[i] can be found in dictionary A using exactly
# one modification in B[i], Else C[i] = '0'.
# NOTE: modification is defined as converting a character into another character.
# 1 <= N <= 30000
# 1 <= M <= 2500
# 1 <= length of any string either in A or B <= 20
# strings contains only lowercase alphabets
# First argument is the string array A.
# Second argument is the string array B.
# Return a binary string C where C[i] = '1' if B[i] can be found in dictionary A using one modification in B[i],
# Else C[i] = '0'.
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
        if self.delete(oldWord) == 0:
            self.insert(newWord)


class Solution:
    # @param A : list of strings
    # @param B : list of strings
    # @return a strings
    def solve(self, A, B):
        node = Trie()
        result = ''

        for word in A:
            node.insert(word)

        for word in B:
            if node.search(word):
                result += '0'
            else:
                tempFlag = False

                for i in range(len(word)):
                    for j in range(26):
                        currChar = chr(97 + j)
                        if currChar == word[i]:
                            continue

                        currWord = word[:i] + currChar + word[i + 1:]
                        if node.search(currWord):
                            result += '1'
                            tempFlag = True
                            break

                    if tempFlag:
                        break

                if not tempFlag:
                    result += '0'

        return result


sol = Solution()
print(sol.solve(['data', 'circle', 'cricket'], ['date', 'circel', 'crikket', 'data', 'circl']))  # '10100'
print(sol.solve(['hello', 'world'], ['hella', 'pello', 'pella']))  # '110'
