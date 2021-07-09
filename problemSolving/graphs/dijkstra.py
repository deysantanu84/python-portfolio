# Given a weighted undirected graph having A nodes and M weighted edges, and a source node C.
# You have to find an integer array D of size A such that:
# => D[i] : Shortest distance form the C node to node i.
# => If node i is not reachable from C then -1.
# Note:
# There are no self-loops in the graph.
# No multiple edges between two pair of vertices.
# The graph may or may not be connected.
# Nodes are numbered from 0 to A-1.
# Your solution will run on multiple testcases. If you are using global variables make sure to clear them.
# 1 <= A <= 1e5
# 0 <= B[i][0],B[i][1] < A
# 0 <= B[i][2] <= 1e3
# 0 <= C < A
# The first argument given is an integer A, representing the number of nodes.
# The second argument given is the matrix B of size M x 3, where nodes B[i][0] and B[i][1]
# are connected with an edge of weight B[i][2].
# The third argument given is an integer C.
# Return the integer array D.
from heapq import heappop, heappush


# TLE
class Solution1:
    # @param A : integer
    # @param B : list of list of integers
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):
        result = []
        visited = {C: 0}
        path = {}

        nodeSet = set()

        for i in range(A):
            nodeSet.add(i)

        edgeList = {i: [] for i in range(A)}
        distanceDict = {}

        for i in range(len(B)):
            edgeList[B[i][0]].append(B[i][1])
            edgeList[B[i][1]].append(B[i][0])
            distanceDict[(B[i][0], B[i][1])] = B[i][2]
            distanceDict[(B[i][1], B[i][0])] = B[i][2]

        while nodeSet:
            minNode = None
            for node in nodeSet:
                if node in visited:
                    if minNode is None:
                        minNode = node

                    elif visited[node] < visited[minNode]:
                        minNode = node

            if minNode is None:
                break

            nodeSet.remove(minNode)
            currentWeight = visited[minNode]

            for edge in edgeList[minNode]:
                weight = currentWeight + distanceDict[(minNode, edge)]
                if edge not in visited or weight < visited[edge]:
                    visited[edge] = weight
                    path[edge] = minNode

        for i in range(A):
            if i in visited:
                result.append(visited[i])
            else:
                result.append(-1)

        return result


class Solution:
    def dijkstra(self, A, B, C):
        graph = {}
        for (u, v), w in B.items():
            if u in graph.keys():
                graph[u].append((w, v))
            else:
                graph[u] = [(w, v)]

            if v in graph.keys():
                graph[v].append((w, u))
            else:
                graph[v] = [(w, u)]

        if C not in graph.keys():
            return [0 if i == C else -1 for i in range(A)]

        visited = [False for _ in range(A + 1)]
        result = [float("inf") for _ in range(A + 1)]
        result[C] = 0
        minHeap = [(result[C], C)]

        while minHeap:
            d, u = heappop(minHeap)
            if visited[u]:
                continue
            visited[u] = True
            for w, v in graph[u]:
                if not visited[v] and result[v] > d + w:
                    result[v] = d + w
                    heappush(minHeap, (result[v], v))

        del result[-1]

        for i in range(len(result)):
            if result[i] == float("inf"):
                result[i] = -1

        return result

    # @param A : integer
    # @param B : list of list of integers
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):
        edges = {}

        for item in B:
            if (item[0], item[1]) in edges.keys():
                edges[(item[0], item[1])] = min(edges[(item[0], item[1])], item[2])
            elif (item[1], item[0]) in edges.keys():
                edges[(item[1], item[0])] = min(edges[(item[1], item[0])], item[2])
            else:
                edges[(item[0], item[1])] = item[2]

        return self.dijkstra(A, edges, C)


sol = Solution()
print(sol.solve(6, [[0, 4, 9], [3, 4, 6], [1, 2, 1], [2, 5, 1], [2, 4, 5], [0, 3, 7], [0, 1, 1], [4, 5, 7], [0, 5, 1]], 4))
# [7, 6, 5, 6, 0, 6]

print(sol.solve(5, [[0, 3, 4], [2, 3, 3], [0, 1, 9], [3, 4, 10], [1, 3, 8]], 4))  # [14, 18, 13, 10, 0]
print(sol.solve(5, [[0, 3, 4], [2, 3, 3], [0, 1, 9], [3, 4, 10], [1, 3, 8]], 10))  # [-1, -1, -1, -1, -1]
print(sol.solve(7, [[2, 4, 10], [3, 4, 1], [3, 6, 1], [1, 2, 4], [4, 5, 6]], 2))  # [-1, 4, 0, 11, 10, 16, 12]
