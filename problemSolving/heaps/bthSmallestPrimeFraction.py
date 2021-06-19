# A sorted array of integers, A contains 1, plus some number of primes.
# Then, for every p < q in the list, we consider the fraction p/q.
# What is the B-th smallest fraction considered?
# Return your answer as an array of integers, where answer[0] = p and answer[1] = q.
# 1 <= length(A) <= 2000
# 1 <= A[i] <= 30000
# 1 <= B <= length(A)*(length(A) - 1)/2
# The first argument of input contains the integer array, A.
# The second argument of input contains an integer B.
# Return an array of two integers, where answer[0] = p and answer[1] = q.
from heapq import heappush, heappop


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        priorityQueue = []
        p = q = 0

        for index, val in enumerate(A):
            heappush(priorityQueue, (1 / val, index, 0, 1, val))

        while B > 0:
            val, row, col, p, q = heappop(priorityQueue)

            if col < len(A):
                if row > col + 1:
                    heappush(priorityQueue, (A[col + 1] / A[row], row, col + 1, A[col + 1], A[row]))
            B -= 1

        return [p, q]


heap = Solution()
print(heap.solve([1, 2, 3, 5], 3))  # [2, 5]
print(heap.solve([1, 7], 1))  # [1, 7]
