# Given an directed graph having A nodes labelled from 1 to A containing M edges given by matrix B
# of size M x 2such that there is a edge directed from node B[i][0] to node B[i][1].
# Find whether a path exists from node 1 to node A.
# Return 1 if path exists else return 0.
# NOTE:
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
# Return 1 if path exists between node 1 to node A else return 0.
class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        queue = [1]
        visited = {}
        neighbours = {}

        for edge in B:
            if edge[0] not in visited:
                visited[edge[0]] = False

            if edge[0] not in neighbours.keys():
                neighbours[edge[0]] = []

            if edge[1] not in visited:
                visited[edge[1]] = False

            neighbours[edge[0]].append(edge[1])

        visited[1] = True

        while queue:
            node = queue.pop(0)

            if node == A:
                return 1

            if node in neighbours.keys():
                for neighbour in neighbours[node]:
                    if not visited[neighbour]:
                        queue.append(neighbour)
                        visited[neighbour] = True

        return 0


sol = Solution()
print(sol.solve(5, [[1, 2], [4, 1], [2, 4], [3, 4], [5, 2], [1, 3]]))  # 0
print(sol.solve(5, [[1, 2], [2, 3], [3, 4], [4, 5]]))  # 1
print(sol.solve(4, [[1, 2], [2, 3], [4, 3]]))  # 0
