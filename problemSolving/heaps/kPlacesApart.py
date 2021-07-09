# Given N persons with different priorities standing in a queue.
# Queue is following a property that Each person is standing atmost B places away from it's sorted position.
# Your task is to sort the queue in the increasing order of priorities.
# NOTE:
# No two persons can have the same priority.
# Use the property of the queue to sort the queue with complexity O(NlogB).
# 1 <= N <= 100000
# 0 <= B <= N
# First argument is an integer array A representing the priorities of N persons.
# Second argument is an integer B.
# Return an integer array representing the sorted queue.
from heapq import heappop, heappush, heapify


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        N = len(A)
        heap = A[:B + 1]
        heapify(heap)
        target = 0

        for index in range(B + 1, N):
            A[target] = heappop(heap)
            heappush(heap, A[index])
            target += 1

        while heap:
            A[target] = heappop(heap)
            target += 1

        return A


sol = Solution()
print(sol.solve([1, 40, 2, 3], 2))  # [1, 2, 3, 40]
print(sol.solve([2, 1, 17, 10, 21, 95], 1))  # [1, 2, 10, 17, 21, 95]
