# Given a matrix of integers A of size N x M describing a maze. The maze consists of empty locations and walls.
# 1 represents a wall in a matrix and 0 represents an empty location in a wall.
# There is a ball trapped in a maze. The ball can go through empty spaces by rolling up, down, left or right,
# but it won't stop rolling until hitting a wall (maze boundary is also considered as a wall).
# When the ball stops, it could choose the next direction.
# Given two array of integers of size B and C of size 2 denoting the starting and destination position of the ball.
# Find the shortest distance for the ball to stop at the destination. The distance is defined by the number
# of empty spaces traveled by the ball from the starting position (excluded) to the destination (included).
# If the ball cannot stop at the destination, return -1.
# 2 <= N, M <= 100
# 0 <= A[i] <= 1
# 0 <= B[i][0], C[i][0] < N
# 0 <= B[i][1], C[i][1] < M
# The first argument given is the integer matrix A.
# The second argument given is an array of integer B.
# The third argument if an array of integer C.
# Return a single integer, the minimum distance required to reach destination
class Solution:
    # @param A : list of list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        pass
