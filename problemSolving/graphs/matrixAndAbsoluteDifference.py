# Given a matrix C of integers, of dimension A x B.
# For any given K, you are not allowed to travel between cells that have an absolute difference greater than K.
# Return the minimum value of K such that it is possible to travel between any pair of cells in the grid
# through a path of adjacent cells.
# NOTE:
# Adjacent cells are those cells that share a side with the current cell.
# 1 <= A, B <= 10^2
# 1 <= C[i][j] <= 10^9
# The first argument given is A.
# The second argument give is B.
# The third argument given is the integer matrix C.
# Return a single integer, the minimum value of K.
import sys
INT_MIN = -sys.maxsize


class Edge:
    def __init__(self, source=0, destination=0, weight=0):
        self.source = source
        self.destination = destination
        self.weight = weight


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
        if node.parent == node:
            return node
        node.parent = self.getLeader(node.parent.vertex)
        return node.parent

    def compareLeader(self, v1, v2):
        if self.getLeader(v1) == self.getLeader(v2):
            return True
        return False


class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of list of integers
    # @return an integer
    def solve(self, A, B, C):
        edgeList = []
        for row in range(A - 1):
            vertex = row * B
            for col in range(B - 1):
                downEdge = Edge()
                downEdge.source = vertex
                downEdge.destination = vertex + B
                downEdge.weight = abs(C[row][col] - C[row + 1][col])
                edgeList.append(downEdge)

                rightEdge = Edge()
                rightEdge.source = vertex
                rightEdge.destination = vertex + 1
                rightEdge.weight = abs(C[row][col] - C[row][col + 1])
                edgeList.append(rightEdge)
                vertex += 1

        for row in range(A - 1):
            vertex = row * B + (B - 1)
            downEdge = Edge()
            downEdge.source = vertex
            downEdge.destination = vertex + B
            downEdge.weight = abs(C[row][B - 1] - C[row + 1][B - 1])
            edgeList.append(downEdge)

        vertex = (A - 1) * B
        for col in range(B - 1):
            rightEdge = Edge()
            rightEdge.source = vertex
            rightEdge.destination = vertex + 1
            rightEdge.weight = abs(C[A - 1][col] - C[A - 1][col + 1])
            edgeList.append(rightEdge)
            vertex += 1

        edgeList.sort(key=lambda x: x.weight)
        totalVertices = A * B
        requiredEdges = A * B - 1
        edgeSet = DisjointSet()
        for i in range(totalVertices):
            edgeSet.makeSet(i)

        edgeIndex = 0
        result = INT_MIN
        numEdges = 0
        while numEdges < requiredEdges:
            edge = edgeList[edgeIndex]
            source = edge.source
            destination = edge.destination
            if not edgeSet.compareLeader(source, destination):
                weight = edge.weight
                edgeSet.unionSet(source, destination)
                result = max(result, weight)
                numEdges += 1
            edgeIndex += 1

        return result


sol = Solution()
print(sol.solve(3, 3, [[1, 5, 6], [10, 7, 2], [3, 6, 9]]))  # 4
# It is possible to travel between any pair of cells through a path of adjacent cells that do not have an absolute
# difference in value greater than 4. e.g. : A path from (0, 0) to (2, 2) may look like this:
# => (0, 0) -> (0, 1) -> (1, 1) -> (2, 1) -> (2, 2)
