# Given a weighted undirected graph having A nodes, a source node C and destination node D.
# Find the shortest distance from C to D and if it is impossible to reach node D from C then return -1.
# You are expected to do it in Time Complexity of O(A + M).
# Note:
# There are no self-loops in the graph.
# No multiple edges between two pair of vertices.
# The graph may or may not be connected.
# Nodes are Numbered from 0 to A-1.
# Your solution will run on multiple testcases. If you are using global variables make sure to clear them.
# 1 <= A <= 10^5
# 0 <= B[i][0], B[i][1] < A
# 1 <= B[i][2] <= 2
# 0 <= C < A
# 0 <= D < A
# The first argument given is an integer A, representing the number of nodes.
# The second argument given is the matrix B, where B[i][0] and B[i][1] are
# connected through an edge of weight B[i][2].
# The third argument given is an integer C, representing the source node.
# The fourth argument is an integer D, representing the destination node.
# Note: B[i][2] will be either 1 or 2.
# Return the shortest distance from C to D. If it is impossible to reach node D from C then return -1.
class Solution:
    def pathLength(self, parent, node, orig):
        length = 1
        if parent[node] == -1 and node < orig:
            return 0

        temp = self.pathLength(parent, parent[node], orig)
        length = temp + length

        return length

    # @param A : integer
    # @param B : list of list of integers
    # @param C : integer
    # @param D : integer
    # @return an integer
    def solve(self, A, B, C, D):
        visited = [False] * A
        parent = [-1] * A
        graph = {i: [] for i in range(A)}
        orig = A

        for i in range(len(B)):
            if B[i][2] == 1:
                graph[B[i][0]].append(B[i][1])
                graph[B[i][1]].append(B[i][0])

            else:
                graph[B[i][0]].append(A)
                graph[B[i][1]].append(A)
                graph[A] = [B[i][0], B[i][1]]
                A += 1
                parent.append(-1)
                visited.append(False)

        queue = [C]
        visited[C] = True

        while queue:
            node = queue.pop(0)
            if node == D:
                return self.pathLength(parent, node, orig)

            for i in graph[node]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
                    parent[i] = node

        return -1


sol = Solution()
print(sol.solve(6, [[2, 5, 1], [1, 3, 1], [0, 5, 2], [0, 2, 2], [1, 4, 1], [0, 1, 1]], 3, 2))  # 4
print(sol.solve(13, [[3, 11, 2], [5, 12, 1], [0, 7, 2], [5, 6, 2], [6, 10, 1], [5, 9, 1]], 9, 4))  # -1
print(sol.solve(2, [[0, 1, 1]], 0, 1))  # 1
print(sol.solve(10, [[5, 6, 2], [0, 2, 1], [4, 6, 1], [3, 7, 1], [7, 9, 2], [2, 6, 2], [7, 8, 2], [3, 6, 2], [4, 7, 1], [3, 8, 1]], 9, 7))  # 2
