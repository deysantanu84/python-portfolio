# Given a undirected graph having A nodes. A matrix B of size M x 2 is given which represents
# the edges such that there is an edge between B[i][0] and B[i][1].
# Find whether the given graph is bipartite or not.
# A graph is bipartite if we can split it's set of nodes into two independent subsets
# A and B such that every edge in the graph has one node in A and another node in B
# Note:
# There are no self-loops in the graph.
# No multiple edges between two pair of vertices.
# The graph may or may not be connected.
# Nodes are Numbered from 0 to A-1.
# Your solution will run on multiple testcases. If you are using global variables make sure to clear them.
# 1 <= A <= 100000
# 1 <= M <= min(A*(A-1)/2,200000)
# 0 <= B[i][0],B[i][1] < A
# The first argument given is an integer A.
# The second argument given is the matrix B.
# Return 1 if the given graph is bipartite else return 0.
N = 10**5 + 5
graph = [[] for _ in range(N)]


class Solution:
    def clean(self, n):
        for i in range(n + 1):
            graph[i] = []

    def makeGraph(self, n, edges):
        self.clean(n)

        for i in range(len(edges)):
            graph[edges[i][0]].append(edges[i][1])
            graph[edges[i][1]].append(edges[i][0])

    def isBipartite(self, n):
        if not n:
            return True
        color = [-1 for _ in range(n)]
        queue = []

        for i in range(n):
            if color[i] != -1:
                continue
            color[i] = 1
            queue.append(i)

            while len(queue):
                x = queue.pop(0)

                for node in graph[x]:
                    if color[node] == -1:
                        color[node] = color[x] ^ 1
                        queue.append(node)
                    elif color[node] == color[x]:
                        return False

        return True

    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        self.makeGraph(A, B)
        if self.isBipartite(A):
            return 1
        else:
            return 0


sol = Solution()
print(sol.solve(2, [[0, 1]]))  # 1
print(sol.solve(3, [[0, 1], [0, 2], [1, 2]]))  # 0
