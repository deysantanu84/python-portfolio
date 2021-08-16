# We want to make a custom contacts finder applications as part of our college project.
# The application must perform two types of operations:
# Type 1: Add name B[i] ,denoted by 0 in vector A where B[i] is a string in vector B denoting a contact name.
# This must store B[i] as a new contact in the application.
# Type 2: Find partial for B[i] ,denoted by 1 in vector A where B[i] is a string in vector B
# denoting a partial name to search the application for. It must count the number of contacts starting with B[i].
# You have been given sequential add and find operations. You need to perform each operation in order.
# And return as an array of integers, answers for each query of type 2(denoted by 1 in A) .
# 1 <= |A| <= 10000
# 1 <= |length of strings in B| <= 10
# First argument is the vector A, which denotes the type of query.
# Second argument is the vector B, which denotes the string for corresponding query.
# Return an array of integers, denoting answers for each query of type 1.
class TrieNode:
    def __init__(self):
        self.children = {}
        self.visited = 0
        self.terminating = False


class Trie:
    def __init__(self):
        self.root = self.getNode()

    @staticmethod
    def getNode():
        return TrieNode()

    @staticmethod
    def getIndex(char):
        return ord(char)

    def insert(self, word):
        temp = self.root

        for i in range(len(word)):
            index = self.getIndex(word[i])

            if index not in temp.children:
                temp.children[index] = self.getNode()

            temp.visited += 1
            temp = temp.children.get(index)

        temp.terminating = True

    def getVisitedCount(self, word):
        temp = self.root
        count = 0

        for i in range(len(word)):
            index = self.getIndex(word[i])

            if not temp or index not in temp.children:
                return 0

            count = temp.visited
            temp = temp.children.get(index)

        return count


class Solution:
    # @param A : list of integers
    # @param B : list of strings
    # @return a list of integers
    def solve(self, A, B):
        node = Trie()
        result = []

        for index in range(len(A)):
            if A[index]:
                result.append(node.getVisitedCount(B[index]))
            else:
                node.insert(B[index])

        return result


sol = Solution()
print(sol.solve([0, 0, 1, 1], ["hack", "hacker", "hac", "hak"]))  # [2, 0]
print(sol.solve([0, 1], ["abcde", "abc"]))  # [1]
