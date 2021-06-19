# Given a sorted matrix of integers A of size N x M and an integer B.
# Each of the rows and columns of matrix A are sorted in ascending order,
# find the Bth smallest element in the matrix.
# NOTE: Return The Bth smallest element in the sorted order, not the Bth distinct element.
# 1 <= N, M <= 500
# 1 <= A[i] <= 10^9
# 1 <= B <= N * M
# The first argument given is the integer matrix A.
# The second argument given is an integer B.
# Return the B-th smallest element in the matrix.
from heapq import heappush, heappushpop


class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        # if not A or not A[0]:
        #     return -1

        maxHeap = []

        for row in range(len(A)):
            for col in range(len(A[0])):
                next = -A[row][col]

                if len(maxHeap) < B:
                    heappush(maxHeap, next)

                elif next > maxHeap[0]:
                    heappushpop(maxHeap, next)

        return -maxHeap[0]


heap = Solution()
print(heap.solve([[9, 11, 15], [10, 15, 17]], 6))  # 17
print(heap.solve([[5, 9, 11], [9, 11, 13], [10, 12, 15], [13, 14, 16], [16, 20, 21]], 12))  # 16
