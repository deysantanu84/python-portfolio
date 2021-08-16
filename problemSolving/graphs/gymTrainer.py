# You are the trainer of a gym and there are A people who come to your gym.
# Some of them are friends because they walk together, and some of them are friends because they talk together.
# But people become possessive about each other, so a person cannot walk with one friend and talk with another.
# Although he can walk with two or more people or talk with two or more people.
# You being the trainer, decided to suggest each one of the 2 possible diets. But friends, being friends will
# always have the same diet as all the other friends are having.
# Find and return the number of ways you can suggest each of them a diet.
# As the number of ways can be huge, return the answer modulo 109+7.
# NOTE: If there is any person who walks with one person and talks with the another person, then you may return 0.
# 1 <= A, N, M <= 10^5
# 1 <= B[i][0], B[i][1], C[i][0], C[i][1] <= A
# The first argument contains an integer A, representing the number of people.
# The second argument contains a 2-D integer array B of size N x 2, where B[i][0] and B[i][1] are friends
# because they walk together.
# The third argument contains a 2-D integer array C of size M x 2, where C[i][0] and C[i][1] are friends
# because they talk together.
# Return an integer representing the number of ways to suggest one of the two diets to the people.
class DisjointSet:
    class Node:
        def __init__(self, vertex=0, rank=0, parent=None):
            self.vertex = vertex
            self.rank = rank
            self.parent = parent

    hashMap = {}

    def makeSet(self, vertex):
        node = self.Node()
        node.vertex = vertex
        node.rank = 0
        node.parent = node
        self.hashMap[vertex] = node

    def unionSet(self, v1, v2):
        l1 = self.getLeader(v1)
        l2 = self.getLeader(v2)
        if l1 == l2:
            return
        if l1.rank > l2.rank:
            l2.parent = l1
        elif l1.rank == l2.rank:
            l1.rank += 1
            l2.parent = l1
        else:
            l1.parent = l2

    def getLeader(self, vertex):
        node = self.hashMap[vertex]
        if not node:
            return node
        if node.parent == node:
            return node
        node.parent = self.getLeader(node.parent.vertex)
        return node.parent

    def compareLeader(self, v1, v2):
        if self.getLeader(v1) == self.getLeader(v2):
            return True
        return False

    def getLeaderVertex(self, vertex):
        return self.getLeader(vertex)

    def ifExists(self, vertex):
        if not self.hashMap[vertex]:
            return False
        return True

    def cleanup(self):
        self.hashMap = {}


def fastMultiply(base, power):
    if power == 1:
        return base
    elif power == 0:
        return 1
    elif power % 2 == 0:
        temp = fastMultiply(base, power/2)
        return (temp * temp) % (10 ** 9 + 7)
    elif power % 2:
        return (base * fastMultiply(base, power - 1)) % (10 ** 9 + 7)


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @param C : list of list of integers
    # @return an integer
    def solve(self, A, B, C):
        hashSet = set()
        nodeSet = DisjointSet()
        for i in range(1, A + 1):
            nodeSet.makeSet(i)

        for i in range(len(B)):
            hashSet.add(B[i][0])
            hashSet.add(B[i][1])
            nodeSet.unionSet(B[i][0], B[i][1])

        for i in range(len(C)):
            if C[i][0] in hashSet or C[i][1] in hashSet:
                return 0
            nodeSet.unionSet(C[i][0], C[i][1])

        hashSet.clear()

        for i in range(1, A + 1):
            hashSet.add(nodeSet.getLeaderVertex(i))

        return fastMultiply(2, len(hashSet))


sol = Solution()
print(sol.solve(4, [[1, 2]], [[3, 4]]))  # 4
# There are four ways to suggest the diet:
# Diet-1 to (1, 2) and Diet-2 to (3, 4).
# Diet-1 to (1, 2) and Diet-1 to (3, 4).
# Diet-2 to (1, 2) and Diet-1 to (3, 4).
# Diet-2 to (1, 2) and Diet-2 to (3, 4).

print(sol.solve(3, [[1, 2]], [[1, 3]]))  # 0
# Person 1 walks with person 2 and talks with person 3. So, we will return 0.
