# You are given N towns (1 to N). All towns are connected via unique directed path as mentioned in the input.
# Given 2 towns find whether you can reach the first town from the second without repeating any edge.
# B C : query to find whether B is reachable from C.
# Input contains an integer array A of size N and 2 integers B and C ( 1 <= B, C <= N ).
# There exist a directed edge from A[i] to i+1 for every 1 <= i < N. Also, it's guaranteed that A[i] <= i.
# NOTE: Array A is 0-indexed.
# 1 <= n <= 100000
# First argument is vector A
# Second argument is integer B
# Third argument is integer C
# Return 1 if reachable, 0 otherwise.
class Solution:
    def pathExists(self, A, B, C, edges):
        if B == C:
            return 1

        queue = [B]
        visited = [0 for _ in range(len(A) + 1)]
        visited[B] = 1

        while len(queue):
            for i in range(len(queue)):
                temp = queue.pop(0)
                if temp == C:
                    return 1

                for node in edges[temp]:
                    if not visited[node]:
                        if node == C:
                            return 1

                        queue.append(node)
                        visited[node] = 1

        return 0

    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        N = len(A)
        edges = {}

        for i in range(N):
            if (i + 1) in edges.keys():
                edges[i + 1].append(A[i])
            else:
                edges[i + 1] = [A[i]]

        return self.pathExists(A, B, C, edges)


sol = Solution()
print(sol.solve([1, 1, 2], 1, 2))  # 0
print(sol.solve([1, 1, 2], 2, 1))  # 1
