# A country consist of N cities connected by N - 1 roads. King of that country want to construct
# maximum number of roads such that the new country formed remains bipartite country.
# Bipartite country is a country, whose cities can be partitioned into 2 sets in such a way,
# that for each road (u, v) that belongs to the country, u and v belong to different sets.
# Also, there should be no multiple roads between two cities and no self loops.
# Return the maximum number of roads king can construct.
# Since the answer could be large return answer % 10^9 + 7.
# NOTE: All cities can be visited from any city.
# 1 <= A <= 10^5
# 1 <= B[i][0], B[i][1] <= N
# First argument is an integer A denoting the number of cities, N.
# Second argument is a 2D array B of size (N-1) x 2 denoting the initial roads i.e.
# there is a road between cities B[i][0] and B[1][1] .
# Return an integer denoting the maximum number of roads king can construct.
import sys
sys.setrecursionlimit(10**8)


class Solution:
    def util(self, neighbours, node, parent, color, colorsList):
        colorsList[color] += 1

        for i in range(len(neighbours[node])):
            if neighbours[node][i] != parent:
                self.util(neighbours, neighbours[node][i], node, not color, colorsList)

    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        colorsList = [0, 0]

        neighbours = {node + 1: [] for node in range(A)}
        for edge in B:
            neighbours[edge[0]].append(edge[1])
            neighbours[edge[1]].append(edge[0])

        self.util(neighbours, 1, 0, 0, colorsList)

        return (colorsList[0] * colorsList[1] - (A - 1)) % (10**9 + 7)


sol = Solution()
print(sol.solve(3, [[1, 2], [1, 3]]))  # 0
print(sol.solve(5, [[1, 3], [1, 4], [3, 2], [3, 5]]))  # 2
