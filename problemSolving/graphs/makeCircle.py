# Given an array of strings A of size N, find if the given strings can be chained to form a circle.
# A string X can be put before another string Y in circle if the last character of X is same as first character of Y.
# NOTE: All strings consist of lower case characters.
# 1 <= N <= 10^5
# Sum of length of all strings <= 10^6
# First and only argument is a string array A of size N.
# Return an integer 1 if it is possible to chain the strings to form a circle else return 0.
class Solution:
    def dfs(self, graph, node, visited):
        visited[node] = True

        for i in range(len(graph[node])):
            if not visited[graph[node][i]]:
                self.dfs(graph, graph[node][i], visited)

    def isConnected(self, graph, mark, node):
        visited = [False for _ in range(26)]
        self.dfs(graph, node, visited)

        for i in range(26):
            if mark[i] != visited[i]:
                return 0

        return 1

    # @param A : list of strings
    # @return an integer
    def solve(self, A):
        graph = [[] for _ in range(26)]
        mark = [False for _ in range(26)]
        inEdges = [0 for _ in range(26)]
        outEdges = [0 for _ in range(26)]

        for i in range(len(A)):
            front = ord(A[i][0]) - ord('a')
            back = ord(A[i][-1]) - ord('a')

            mark[front] = True
            mark[back] = True

            outEdges[front] += 1
            inEdges[back] += 1

            graph[front].append(back)

        for i in range(26):
            if inEdges[i] != outEdges[i]:
                return 0

        return self.isConnected(graph, mark, ord(A[0][0]) - ord('a'))


sol = Solution()
print(sol.solve(["aab", "bac", "aaa", "cda"]))  # 1
print(sol.solve(["abc", "cbc"]))  # 0
