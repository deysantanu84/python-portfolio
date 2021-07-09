# Find largest distance Given an arbitrary unweighted rooted tree which consists of N (2 <= N <= 40000) nodes.
# The goal of the problem is to find largest distance between two nodes in a tree.
# Distance between two nodes is a number of edges on a path between the nodes
# (there will be a unique path between any pair of nodes since it is a tree).
# The nodes will be numbered 0 through N - 1.
# The tree is given as an array A, there is an edge between nodes A[i] and i (0 <= i < N).
# Exactly one of the i's will have A[i] equal to -1, it will be root node.
# 2 <= |A| <= 40000
# First and only argument is vector A
# Return the length of the longest path
import sys
sys.setrecursionlimit(10**5)


class Solution:
    def topTwoMax(self, firstMax, secondMax, newItem):
        if newItem > firstMax:
            return newItem, firstMax

        elif newItem > secondMax:
            return firstMax, newItem

        else:
            return firstMax, secondMax

    def breadthFirstSearch(self, index, edges):
        if index not in edges:
            return 0, 1

        firstMax = 0
        secondMax = 0
        temp = 0

        for child in edges[index]:
            x, y = self.breadthFirstSearch(child, edges)
            firstMax, secondMax = self.topTwoMax(firstMax, secondMax, y)
            temp = max(temp, x)

        if index != -1:
            return max(temp, firstMax + secondMax), firstMax + 1

        else:
            return temp, firstMax + 1

    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        edges = {}
        for item, edge in enumerate(A):
            if edge in edges.keys():
                edges[edge].append(item)
            else:
                edges[edge] = [item]

        if len(A) > 1:
            return self.breadthFirstSearch(-1, edges)[0]

        return 0


sol = Solution()
print(sol.solve([-1, 0]))  # 1
print(sol.solve([-1, 0, 0]))  # 2
