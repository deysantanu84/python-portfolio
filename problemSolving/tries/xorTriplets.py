# Given an array of integers A of size N.
# A triplet (i, j, k), i <= j <= k is called a power triplet if A[i] ^ A[i+1] ^....A[j-1] = A[j] ^.....^A[k].
# Where, ^ denotes bitwise xor.
# Return the count of all possible power triplets. Since the answer could be large return answer % 10^9 +7.
# 1 <= N <= 100000
# 1 <= A[i] <= 100000
# The first argument given is the integer array A.
# Return the count of all possible power triplets % 109 + 7.
class TrieNode:
    def __init__(self):
        self.children = [None, None]
        self.sumOfIndexes = 0
        self.numberOfIndexes = 0


def insert(node, num, index):
    for bits in range(20, -1, -1):
        curr = (num >> bits) & 1

        if not node.children[curr]:
            node.children[curr] = TrieNode()

        node = node.children[curr]

    node.sumOfIndexes += index
    node.numberOfIndexes += 1


def query(node, num, index):
    for bits in range(20, -1, -1):
        curr = (num >> bits) & 1

        if not node.children[curr]:
            return 0

        node = node.children[curr]

    size = node.numberOfIndexes
    indexSum = node.sumOfIndexes
    result = (size * index) - indexSum

    return result


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        currXor = 0
        result = 0
        root = TrieNode()

        for index in range(len(A)):
            temp = A[index]
            insert(root, currXor, index)
            currXor ^= temp
            result += query(root, currXor, index)
            result %= (10 ** 9 + 7)

        return result


sol = Solution()
print(sol.solve([5, 2, 7]))  # 2
print(sol.solve([1, 2, 3]))  # 2
print(sol.solve([804, 621, 170, 320, 234, 81, 57, 175, 513, 189, 163, 610, 656, 52, 957, 632, 33, 920, 280,
                 317, 931, 848, 630, 511, 251, 754, 899, 648, 284, 598, 818, 428, 18, 996, 629, 203, 449,
                 925, 25, 961, 451, 80, 625, 284, 945, 190, 650, 501, 265, 56, 919, 803, 762, 514, 973, 564,
                 356, 775, 538, 550, 755, 903, 106, 365, 230, 174, 882, 918, 290, 775, 169, 251, 477, 49, 107,
                 967, 368, 432, 272, 5, 556, 223, 460, 812, 848, 853, 513, 470, 833, 966, 786, 641, 916, 892,
                 448, 973, 488, 669, 819, 687]))  # 180
