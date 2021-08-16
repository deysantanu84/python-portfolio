# A students applied for admission in IB Academy. An array of integers B is given representing the
# strengths of A people i.e. B[i] represents the strength of ith student.
# Among the A students some of them knew each other. A matrix C of size M x 2 is given which represents
# relations where ith relations depicts that C[i][0] and C[i][1] knew each other.
# All students who know each other are placed in one batch.
# Strength of a batch is equal to sum of the strength of all the students in it.
# Now the number of batches are formed are very much, it is impossible for IB to handle them.
# So IB set criteria for selection: All those batches having strength at least D are selected.
# Find the number of batches selected.
# NOTE: If student x and student y know each other, student y and z know each other then student x
# and student z will also know each other.
# 1 <= A <= 10^5
# 1 <= M <= 2*10^5
# 1 <= B[i] <= 10^4
# 1 <= C[i][0], C[i][1] <= A
# 1 <= D <= 10^9
# The first argument given is an integer A.
# The second argument given is an integer array B.
# The third argument given is a matrix C.
# The fourth argument given is an integer D.
# Return the number of batches selected in IB.
class Solution:
    tempSum = 0

    def dfs(self, source, graph, visited, B):
        visited[source] = True
        Solution.tempSum += B[source - 1]

        for node in graph[source]:
            if not visited[node]:
                self.dfs(node, graph, visited, B)

    # @param A : integer
    # @param B : list of integers
    # @param C : list of list of integers
    # @param D : integer
    # @return an integer
    def solve(self, A, B, C, D):
        result = 0
        graph = {}
        visited = [False for _ in range(A + 1)]

        for i in range(1, A + 1):
            graph[i] = set()

        for i in range(len(C)):
            graph[C[i][0]].add(C[i][1])

        for i in range(1, A + 1):
            if not visited[i]:
                Solution.tempSum = 0
                self.dfs(i, graph, visited, B)
                if Solution.tempSum >= D:
                    result += 1

        return result


sol = Solution()
print(sol.solve(7, [1, 6, 7, 2, 9, 4, 5], [[1, 2], [2, 3], [5, 6], [5, 7]], 12))  # 2
print(sol.solve(5, [1, 2, 3, 4, 5], [[1, 5], [2, 3]], 6))  # 1
print(sol.solve(14, [7, 5, 7, 3, 9, 4, 4, 6, 3, 1, 4, 8, 7, 6],
                [[1, 2], [2, 6], [2, 7], [4, 13], [5, 8], [5, 13], [6, 12], [7, 10], [10, 14], [13, 14]], 2))  # 4
