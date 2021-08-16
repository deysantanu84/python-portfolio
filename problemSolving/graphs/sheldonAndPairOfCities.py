# Sheldon lives in a country with A cities (numbered from 1 to A) and B bidirectional roads.
# Roads are denoted by integer array D, E and F of size M, where D[i] and E[i] denotes the cities and
# F[i] denotes the distance between the cities.
# Now he has many lectures to give in the city and is running short of time, so he asked you C queries,
# for each query i, find the shortest distance between city G[i] and H[i].
# If the two cities are not connected then the distance between them is assumed to be -1.
# 1 <= A <= 200
# 1 <= B <= 200000
# 1 <= C <= 100000
# 1 <= F[i] <= 1000000
# 1 <= D[i], E[i], G[i], H[i] <= A
# First argument is an integer A.
# Second argument is an integer B.
# Third argument is an integer C.
# Fourth argument is an integer array D.
# Fifth argument is an integer array E.
# Sixth argument is an integer array F.
# Seventh argument is an integer array G.
# Eight argument is an integer array H.
# Return an integer array of size C, for each query denoting the shortest distance between the given two vertices.
# If the two vertices are not connected then output -1.
import sys
INT_MAX = sys.maxsize - 1


class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : list of integers
    # @param E : list of integers
    # @param F : list of integers
    # @param G : list of integers
    # @param H : list of integers
    # @return a list of integers
    def solve(self, A, B, C, D, E, F, G, H):
        dist = [[INT_MAX for _ in range(A + 1)] for _ in range(A + 1)]

        for i in range(A + 1):
            dist[i][i] = 0

        for i in range(B):
            if F[i] < dist[D[i]][E[i]]:
                dist[D[i]][E[i]] = F[i]
                dist[E[i]][D[i]] = F[i]

        for k in range(1, A + 1):
            for i in range(1, A + 1):
                for j in range(1, A + 1):
                    if dist[i][k] != INT_MAX and dist[k][j] != INT_MAX and dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        result = [0 for _ in range(C)]
        for i in range(C):
            if dist[G[i]][H[i]] != INT_MAX:
                result[i] = dist[G[i]][H[i]]
            else:
                result[i] = -1

        return result


sol = Solution()
print(sol.solve(4, 6, 2, [1, 2, 3, 2, 4, 3], [2, 3, 4, 4, 1, 1], [4, 1, 1, 1, 1, 1], [1, 1], [2, 3]))  # [2, 1]
print(sol.solve(3, 3, 2, [1, 2, 1], [2, 3, 3], [3, 1, 1], [2, 1], [3, 2]))  # [1, 2]
