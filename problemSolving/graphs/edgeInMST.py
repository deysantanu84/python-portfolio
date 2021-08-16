# Given a undirected weighted graph with A nodes labelled from 1 to A with M edges given in a form of
# 2D-matrix B of size M * 3 where B[i][0] and B[i][1] denotes the two nodes connected by an edge of weight B[i][2].
# For each edge check whether it belongs to any of the possible minimum spanning tree or not , return 1
# if it belongs else return 0.
# Return an one-dimensional binary array of size M denoting answer for each edge.
# NOTE:
# The graph may be disconnected in that case consider mst for each component.
# No self-loops and no multiple edges present.
# Answers in output array must be in order with the input array B output[i] must denote the answer of
# edge B[i][0] to B[i][1].
# 1 <= A, M <= 3*10^5
# 1 <= B[i][0], B[i][1] <= A
# 1 <= B[i][1] <= 10^3
# The first argument given is an integer A representing the number of nodes in the graph.
# The second argument given is an matrix B of size M x 3 which represents the M edges such that
# there is a edge between node B[i][0] and node B[i][1] with weight B[i][2].
# Return an one-dimensional binary array of size M denoting answer for each edge.
from functools import cmp_to_key


class Solution:
    parent = []
    height = []

    @staticmethod
    def createSet(A):
        Solution.parent = [0 for _ in range(A + 1)]
        Solution.height = [0 for _ in range(A + 1)]

        for i in range(1, A + 1):
            Solution.parent[i] = i
            Solution.height[i] = 0

    def find(self, item):
        if item == Solution.parent[item]:
            return item

        Solution.parent[item] = self.find(Solution.parent[item])
        return Solution.parent[item]

    @staticmethod
    def compare(x, y):
        if x[2] == y[2]:
            return 0
        elif x[2] < y[2]:
            return -1
        else:
            return 1

    # @param A : integer
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        self.createSet(A)
        edgeIndexMap = {}
        indexEdgeMap = {}
        parent = Solution.parent
        height = Solution.height

        for i in range(len(B)):
            edgeIndexMap[tuple(B[i])] = i
            indexEdgeMap[i] = B[i]

        B.sort(key=cmp_to_key(self.compare))
        result = [0 for _ in range(len(B))]
        minCost = 0
        for i in range(len(B)):
            edge = B[i]
            u = edge[0]
            v = edge[1]
            w = edge[2]
            parentU = self.find(u)
            parentV = self.find(v)
            j = edgeIndexMap[tuple(edge)]
            if parentU == parentV:
                result[j] = 0
            else:
                result[j] = 1
                if height[parentU] < height[parentV]:
                    parent[parentU] = parentV
                elif height[parentV] < height[parentU]:
                    parent[parentV] = parentU
                else:
                    parent[parentU] = parentV
                    height[parentV] += 1
                minCost += w

        for i in range(len(result)):
            if result[i] == 0:
                edge = indexEdgeMap[i]
                cost = edge[2]
                self.createSet(A)
                parent[edge[1]] = edge[0]
                for j in range(len(B)):
                    parentU = self.find(B[j][0])
                    parentV = self.find(B[j][1])
                    if parentU == parentV:
                        continue
                    if height[parentU] < height[parentV]:
                        parent[parentU] = parentV
                    elif height[parentV] < height[parentU]:
                        parent[parentV] = parentU
                    else:
                        parent[parentU] = parentV
                        height[parentV] += 1
                    cost += B[j][2]
                    if cost > minCost:
                        break
                if cost == minCost:
                    result[i] = 1

        return result


sol = Solution()
print(sol.solve(3, [[1, 2, 2], [1, 3, 2], [2, 3, 3]]))  # [1, 1, 0]
