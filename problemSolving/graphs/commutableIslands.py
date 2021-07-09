# There are A islands and there are M bridges connecting them. Each bridge has some cost attached to it.
# We need to find bridges with minimal cost such that all islands are connected.
# It is guaranteed that input data will contain at least one possible scenario in which
# all islands are connected with each other.
# 1 <= A, M <= 6*10^4
# 1 <= B[i][0], B[i][1] <= A
# 1 <= B[i][2] <= 10^3
# The first argument contains an integer, A, representing the number of islands.
# The second argument contains an 2-d integer matrix, B, of size M x 3 where Island B[i][0]
# and B[i][1] are connected using a bridge of cost B[i][2].
# Return an integer representing the minimal cost required.
class Solution:
    class Edges(list):
        def __lt__(self, other):
            for i in [2, 0, 1]:
                if self[i] == other[i]:
                    continue
                return self[i] < other[i]

    class DisjointSet:
        def __init__(self, i):
            self.parent = i
            self.level = 0

        def __repr__(self):
            return "{}<{}>".format(self.parent, self.level)

    def findSet(self, x, S):
        if S[x].parent == x:
            return x

        S[x].parent = self.findSet(S[x].parent, S)
        return S[x].parent

    def unionSet(self, a, b, S):
        setA = self.findSet(a, S)
        setB = self.findSet(b, S)

        if S[setA].level < S[setB].level:
            S[setA].parent = setB

        elif S[setA].level > S[setB].level:
            S[setB].parent = setA

        else:
            S[setB].parent = setA
            S[setA].level += 1

    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        B.sort(key=Solution.Edges)
        S = [None] + [Solution.DisjointSet(i + 1) for i in range(A)]
        components = A - 1
        cost = 0

        for edge in B:
            if components == 0:
                break

            start = self.findSet(edge[0], S)
            end = self.findSet(edge[1], S)

            if start == end:
                continue

            self.unionSet(start, end, S)
            components -= 1
            cost += edge[2]

        return cost


sol = Solution()
print(sol.solve(4, [[1, 2, 1], [2, 3, 4], [1, 4, 3], [4, 3, 2], [1, 3, 10]]))  # 6
print(sol.solve(4, [[1, 2, 1], [2, 3, 2], [3, 4, 4], [1, 4, 3]]))  # 6
