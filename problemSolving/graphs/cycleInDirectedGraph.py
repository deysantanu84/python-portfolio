# Given an directed graph having A nodes. A matrix B of size M x 2 is given which represents the
# M edges such that there is a edge directed from node B[i][0] to node B[i][1].
# Find whether the graph contains a cycle or not, return 1 if cycle is present else return 0.
# NOTE:
# The cycle must contain atleast two nodes.
# There are no self-loops in the graph.
# There are no multiple edges between two nodes.
# The graph may or may not be connected.
# Nodes are numbered from 1 to A.
# Your solution will run on multiple test cases. If you are using global variables make sure to clear them.
# 2 <= A <= 10^5
# 1 <= M <= min(200000,A*(A-1))
# 1 <= B[i][0], B[i][1] <= A
# The first argument given is an integer A representing the number of nodes in the graph.
# The second argument given a matrix B of size M x 2 which represents the M edges such that
# there is a edge directed from node B[i][0] to node B[i][1].
# Return 1 if cycle is present else return 0.
import sys
sys.setrecursionlimit(10**8)


class Solution:
    def isCyclicUtil(self, node, visited, stack, neighbours):
        visited[node] = True
        stack[node] = True

        for neighbour in neighbours[node]:
            if not visited[neighbour]:
                if self.isCyclicUtil(neighbour, visited, stack, neighbours):
                    return True

            elif stack[neighbour]:
                return True

        stack[node] = False
        return False

    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        visited = [False] * (A + 1)
        stack = [False] * (A + 1)
        neighbours = {vertex + 1: [] for vertex in range(A)}

        for edge in B:
            neighbours[edge[0]].append(edge[1])

        for node in range(1, A + 1):
            if not visited[node]:
                if self.isCyclicUtil(node, visited, stack, neighbours):
                    return 1

        return 0


sol = Solution()
print(sol.solve(5, [[1, 2], [4, 1], [2, 4], [3, 4], [5, 2], [1, 3]]))  # 1
print(sol.solve(5, [[1, 2], [2, 3], [3, 4], [4, 5]]))  # 0
