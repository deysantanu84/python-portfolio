# There is a rectangle with left bottom as (0, 0) and right up as (x, y).
# There are N circles such that their centers are inside the rectangle.
# Radius of each circle is R. Now we need to find out if it is possible that
# we can move from (0, 0) to (x, y) without touching any circle.
# Note : We can move from any cell to any of its 8 adjacent neighbours and
# we cannot move outside the boundary of the rectangle at any point of time.
# 0 <= x , y, R <= 100
# 1 <= N <= 1000
# Center of each circle would lie within the grid
# 1st argument given is an Integer x , denoted by A in input.
# 2nd argument given is an Integer y, denoted by B in input.
# 3rd argument given is an Integer N, number of circles, denoted by C in input.
# 4th argument given is an Integer R, radius of each circle, denoted by D in input.
# 5th argument given is an Array A of size N, denoted by E in input, where A[i] = x coordinate of ith circle
# 6th argument given is an Array B of size N, denoted by F in input, where B[i] = y coordinate of ith circle
# Return YES or NO depending on weather it is possible to reach cell (x,y) or not starting from (0,0).
from math import sqrt
import sys
sys.setrecursionlimit(10**8)


class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @param E : list of integers
    # @param F : list of integers
    # @return a strings
    def solve(self, A, B, C, D, E, F):
        result = [[0 for _ in range(B + 1)] for _ in range(A + 1)]
        queue = []

        for i in range(A + 1):
            for j in range(B + 1):
                for k in range(C):
                    if sqrt(pow((E[k] - i), 2) + pow((F[k] - j), 2)) <= D:
                        result[i][j] = -1

        if result[0][0] == -1:
            return "NO"

        queue.append((0, 0))
        result[0][0] = 1

        while len(queue):
            a, b = queue.pop()

            if a and b and result[a - 1][b - 1] == 0:
                result[a - 1][b - 1] = 1
                queue.append((a - 1, b - 1))

            if a + 1 <= A and b + 1 <= B and result[a + 1][b + 1] == 0:
                result[a + 1][b + 1] = 1
                queue.append((a + 1, b + 1))

            if a and result[a - 1][b] == 0:
                result[a - 1][b] = 1
                queue.append((a - 1, b))

            if b and result[a][b - 1] == 0:
                result[a][b - 1] = 1
                queue.append((a, b - 1))

            if a and b + 1 <= B and result[a - 1][b + 1] == 0:
                result[a - 1][b + 1] = 1
                queue.append((a - 1, b + 1))

            if b + 1 <= B and result[a][b + 1] == 0:
                result[a][b + 1] = 1
                queue.append((a, b + 1))

            if a + 1 <= A and b and result[a + 1][b - 1] == 0:
                result[a + 1][b - 1] = 1
                queue.append((a + 1, b - 1))

            if a + 1 <= A and result[a + 1][b] == 0:
                result[a + 1][b] = 1
                queue.append((a + 1, b))

        if result[A][B] == 1:
            return "YES"
        else:
            return "NO"


sol = Solution()
print(sol.solve(2, 3, 1, 1, [2], [3]))  # NO
print(sol.solve(1, 1, 1, 1, [1], [1]))  # NO
print(sol.solve(1, 1, 1, 1, [0], [0]))  # NO
