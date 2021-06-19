# Given two integers arrays A and B of size N each.
# Find the maximum N elements from the sum combinations (Ai + Bj) formed from elements in array A and B.
# 1 <= N <= 2 * 10^5
# -1000 <= A[i], B[i] <= 1000
# First argument is an integer array A.
# Second argument is an integer array B.
# Return an integer array denoting the N maximum element in descending order.
from heapq import heappush, heappop


class MaxHeap(tuple):
    def __lt__(self, other):
        return self[0] > other[0]


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        result = []
        A.sort(reverse=True)
        B.sort(reverse=True)

        heap = []
        seen = set()

        heappush(heap, MaxHeap((A[0] + B[0], (0, 0))))
        seen.add((0, 0))

        for _ in range(len(A)):
            entry, index = heappop(heap)
            x, y = index
            result.append(entry)

            if x + 1 < len(A) and (x + 1, y) not in seen:
                heappush(heap, MaxHeap((A[x + 1] + B[y], (x + 1, y))))
                seen.add((x + 1, y))

            if y + 1 < len(B) and (x, y + 1) not in seen:
                heappush(heap, MaxHeap((A[x] + B[y + 1], (x, y + 1))))
                seen.add((x, y + 1))

        return result


sol = Solution()
print(sol.solve([1, 4, 2, 3], [2, 5, 1, 6]))  # [10, 9, 9, 8]
print(sol.solve([2, 4, 1, 1], [-2, -3, 2, 4]))  # [8, 6, 6, 5]
