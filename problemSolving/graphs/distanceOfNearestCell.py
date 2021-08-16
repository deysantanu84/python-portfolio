# Given a matrix of integers A of size N x M consisting of 0 or 1.
# For each cell of the matrix find the distance of nearest 1 in the matrix.
# Distance between two cells (x1, y1) and (x2, y2) is defined as |x1 - x2| + |y1 - y2|.
# Find and return a matrix B of size N x M which defines for each cell in A
# distance of nearest 1 in the matrix A.
# NOTE: There is at least one 1 is present in the matrix.
# 1 <= N, M <= 1000
# 0 <= A[i][j] <= 1
# The first argument given is the integer matrix A.
# Return the matrix B.
# TLE
import sys
INT_MAX = sys.maxsize


class Solution1:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        rowCount = len(A)
        colCount = len(A[0])
        newX = [-1, 0, 1, 0]
        newY = [0, -1, 0, 1]
        queue = []
        resultGrid = [[0 for _ in range(colCount)] for _ in range(rowCount)]

        for i in range(rowCount):
            for j in range(colCount):
                resultGrid[i][j] = INT_MAX
                if A[i][j] == 1:
                    resultGrid[i][j] = 0
                    queue.append([i, j])

        while len(queue):
            popped = queue.pop(0)

            x = popped[0]
            y = popped[1]

            for i in range(4):
                adjX = x + newX[i]
                adjY = y + newY[i]

                if 0 <= adjX < rowCount and 0 <= adjY < colCount \
                        and resultGrid[adjX][adjY] > resultGrid[x][y] + 1:
                    resultGrid[adjX][adjY] = resultGrid[x][y] + 1
                    queue.append([adjX, adjY])

        return resultGrid


class Solution2:
    def generateGraph(self, graph, rows, cols):
        k = 1

        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                if i == rows:
                    if j != cols:
                        graph[k].append(k + 1)
                        graph[k + 1].append(k)

                elif j == cols:
                    graph[k].append(k + cols)
                    graph[k + cols].append(k)

                else:
                    graph[k].append(k + 1)
                    graph[k + 1].append(k)
                    graph[k].append(k + cols)
                    graph[k + cols].append(k)

                k += 1

    def bfs(self, visited, dist, queue, graph):
        while len(queue):
            temp = queue.pop(0)

            for i in graph[temp]:
                if visited[i] != 1:
                    dist[i] = min(dist[i], dist[temp] + 1)
                    queue.append(i)
                    visited[i] = 1

        return dist

    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        rows = len(A)
        cols = len(A[0])

        graph = [[] for _ in range(rows * cols + 1)]
        self.generateGraph(graph, rows, cols)
        dist = [0] * (rows * cols + 1)
        visited = [0] * (rows * cols + 1)

        for i in range(1, cols * rows + 1):
            dist[i] = 10 ** 9
            visited[i] = 0

        k = 1
        queue = []

        for i in range(rows):
            for j in range(cols):
                if A[i][j] == 1:
                    dist[k] = 0
                    visited[k] = 1
                    queue.append(k)

                k += 1

        dist = self.bfs(visited, dist, queue, graph)

        result = []
        row = []
        col = 1
        for i in range(1, rows * cols + 1):
            row.append(dist[i])
            if not col % cols:
                result.append(row)
                row = []

            col += 1

        return result


class Solution:
    def isSafe(self, currRow, currCol, rows, cols):
        return 0 <= currRow < rows and 0 <= currCol < cols

    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        rows = len(A)
        cols = len(A[0])
        result = [[-1 for _ in range(cols)] for _ in range(rows)]
        queue = []

        for i in range(rows):
            for j in range(cols):
                if A[i][j]:
                    result[i][j] = 0
                    queue.append((i, j))

        rowsList = [0, -1, 0, 1]
        colsList = [1, 0, -1, 0]
        currDist = 1

        while len(queue):
            temp = []
            while len(queue):
                row, col = queue.pop()
                for i in range(4):
                    if self.isSafe(row + rowsList[i], col + colsList[i], rows, cols):
                        if result[row + rowsList[i]][col + colsList[i]] == -1:
                            result[row + rowsList[i]][col + colsList[i]] = currDist
                            temp.append((row + rowsList[i], col + colsList[i]))

            queue = temp
            currDist += 1

        return result


sol = Solution()
print(sol.solve([[0, 0, 0, 1], [0, 0, 1, 1], [0, 1, 1, 0]]))
# [[3, 2, 1, 0], [2, 1, 0, 0], [1, 0, 0, 1]]

print(sol.solve([[1, 0, 0], [0, 0, 0], [0, 0, 0]]))
# [[0, 1, 2], [1, 2, 3], [2, 3, 4]]
