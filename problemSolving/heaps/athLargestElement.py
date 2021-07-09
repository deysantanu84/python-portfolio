# Given an integer array B of size N.
# You need to find the Ath largest element in the subarray [1 to i] where i varies from 1 to N.
# In other words, find the Ath largest element in the sub-arrays [1 : 1], [1 : 2], [1 : 3], ...., [1 : N].
# NOTE: If any subarray [1 : i] has less than A elements then output array should be -1 at the ith index.
# 1 <= N <= 100000
# 1 <= A <= N
# 1 <= B[i] <= INT_MAX
# First argument is an integer A.
# Second argument is an integer array B of size N.
# Return an integer array C, where C[i] (1 <= i <= N) will have the
# Ath largest element in the subarray [1 : i].
from heapq import heappush, heappop


class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        N = len(B)
        result = []
        heap = []

        for i in range(N):
            if len(heap) < A:
                heappush(heap, B[i])
            else:
                if B[i] > heap[0]:
                    heappop(heap)
                    heappush(heap, B[i])

            if len(heap) < A:
                result.append(-1)
            else:
                result.append(heap[0])

        return result


sol = Solution()
print(sol.solve(4, [1, 2, 3, 4, 5, 6]))  # [-1, -1, -1, 1, 2, 3]
print(sol.solve(2, [15, 20, 99, 1]))  # [-1, 15, 20, 20]
