# Given an directed acyclic graph having A nodes. A matrix B of size M x 2 is given which represents
# the M edges such that there is a edge directed from node B[i][0] to node B[i][1].
# Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that
# for every directed edge uv, vertex u comes before v in the ordering.
# Topological Sorting for a graph is not possible if the graph is not a DAG.
# Return the topological ordering of the graph and if it doesn't exist then return an empty array.
# If there is a solution return the correct ordering. If there are multiple solutions print
# the lexicographically smallest one.
# Ordering (a, b, c) is said to be lexicographically smaller than ordering (e, f, g)
# if a < e or if(a==e) then b < f and so on.
# NOTE:
# There are no self-loops in the graph.
# There are no multiple edges between two nodes.
# The graph may or may not be connected.
# Nodes are numbered from 1 to A.
# Your solution will run on multiple test cases. If you are using global variables make sure to clear them.
# 2 <= A <= 10^4
# 1 <= M <= min(100000,A*(A-1))
# 1 <= B[i][0], B[i][1] <= A
# The first argument given is an integer A representing the number of nodes in the graph.
# The second argument given a matrix B of size M x 2 which represents the M edges such
# that there is a edge directed from node B[i][0] to node B[i][1].
# Return a one-dimensional array denoting the topological ordering of the graph and
# if it doesn't exist then return empty array.
class Solution:
    def topologicalSortUtil(self, node, visited, stack, neighbours):
        visited[node] = True

        for neighbour in neighbours[node]:
            if not visited[neighbour]:
                self.topologicalSortUtil(neighbour, visited, stack, neighbours)

        stack.append(node)

    # @param A : integer
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        visited = [False] * (A + 1)
        resultStack = []

        neighbours = {vertex + 1: [] for vertex in range(A)}
        for edge in B:
            neighbours[edge[0]].append(edge[1])

        for node in range(1, A + 1):
            if not visited[node - 1]:
                self.topologicalSortUtil(node, visited, resultStack, neighbours)

        return resultStack[::-1]


sol = Solution()
print(sol.solve(6, [[6, 3], [6, 1], [5, 1], [5, 2], [3, 4], [4, 2]]))  # [5, 6, 1, 3, 4, 2]
print(sol.solve(3, [[1, 2], [2, 3], [3, 1]]))  # []
