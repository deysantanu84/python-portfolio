# Given an array A of integers of size N. Find the subarray AL, AL+1, AL+2, ... AR with 1<=L<=R<=N
# which has maximum XOR value.
# NOTE: If there are multiple subarrays with same maximum value, return the subarray with minimum length.
# If length is same, return the subarray with minimum starting index.
# 1 <= N <= 100000
# 0 <= A[i] <= 10^9
# First and only argument is an integer array A.
# Return an integer array B of size 2. B[0] is the starting index(1-based) of the subarray
# and B[1] is the ending index(1-based) of the subarray.
class TrieNode:
    def __init__(self):
        self.children = {}
        self.leaf = 0


class Trie:
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()

    def insert(self, n):
        temp = self.root

        for i in range(31, -1, -1):
            index = self.check(n, i)
            if index not in temp.children:
                temp.children[index] = self.getNode()
            temp = temp.children.get(index)

        temp.leaf = True

    def check(self, n, index):
        if n & (1 << index):
            return True
        else:
            return False

    def getXorValue(self, n):
        temp = self.root
        result = 0

        for i in range(31, -1, -1):
            flag = self.check(n, i)
            index = flag ^ 1

            if index not in temp.children:
                temp = temp.children.get(index ^ 1)

            else:
                result += (1 << i)
                temp = temp.children.get(index)

        return result


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        N = len(A)

        for index in range(1, N):
            A[index] ^= A[index-1]

        result = [1, 1]
        maxXor = A[0]

        node = Trie()
        node.insert(A[0])

        indexDict = {A[0]: 0}

        for index in range(1, N):
            indexDict[A[index]] = index
            if A[index] > maxXor:
                maxXor = A[index]
                result = [1, index + 1]

            elif A[index] == maxXor:
                if result[0] != result[1]:
                    result = [index + 1, index + 1]

            currMaxXor = node.getXorValue(A[index])
            j = indexDict[currMaxXor ^ A[index]]
            j += 1

            if currMaxXor > maxXor:
                maxXor = currMaxXor
                result = [j + 1, index + 1]

            elif currMaxXor == maxXor:
                currLen = index - j + 1
                resultLen = result[1] - result[0] + 1
                if currLen < resultLen:
                    result = [j + 1, index + 1]
            node.insert(A[index])

        return result


sol = Solution()
print(sol.solve([1, 4, 3]))  # [2, 3]
print(sol.solve([8]))  # [1, 1]
print(sol.solve([8, 1, 2, 12]))  # [2, 4]
print(sol.solve([33, 29, 18]))  # [1, 2]
