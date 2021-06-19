# We have a list A, of points(x,y) on the plane. Find the B closest points to the origin (0, 0).
# Here, the distance between two points on a plane is the Euclidean distance.
# You may return the answer in any order. The answer is guaranteed to be unique
# (except for the order that it is in.)
# NOTE: Euclidean distance between two points P1(x1,y1) and P2(x2,y2) is sqrt( (x1-x2)^2 + (y1-y2)^2 ).
# 1 <= B <= length of the list A <= 100000
# -100000 <= A[i][0] <= 100000
# -100000 <= A[i][1] <= 100000
# The argument given is list A and an integer B.
# Return the B closest points to the origin (0, 0) in any order.
from heapq import heappushpop, heappush


class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return a list of list of integers
    def solve(self, A, B):
        minHeap = []

        for (p, q) in A:
            distance = -(p**2 + q**2)

            if len(minHeap) == B:
                heappushpop(minHeap, (distance, p, q))

            else:
                heappush(minHeap, (distance, p, q))

        return [[p, q] for (distance, p, q) in minHeap]


heap = Solution()
print(heap.solve([[1, 3], [-2, 2]], 1))  # [[-2, 2]]
print(heap.solve([[1, -1], [2, -1]], 1))  # [[1, -1]]
