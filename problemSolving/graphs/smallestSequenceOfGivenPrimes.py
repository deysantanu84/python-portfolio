# Given three prime number(A, B, C) and an integer D. Find the first(smallest) D integers
# which have only A, B, C or a combination of them as their prime factors.
# 1 <= A, B, C <= 10000
# 1 <= D <= 100000
# First argument is an integer A.
# Second argument is an integer B.
# Third argument is an integer C.
# Fourth argument is an integer D.
# Return an integer array of size D, denoting the first D integers described above.
# NOTE: The sequence should be sorted in ascending order
from heapq import heappop, heappush, heapify


class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @return a list of integers
    def solve(self, A, B, C, D):
        nums = [A, B, C]
        result = []
        finished = set()
        i = 0
        heap = list(nums)
        heapify(heap)

        while i < D:
            curr = heappop(heap)
            if curr in finished:
                continue

            result.append(curr)
            finished.add(curr)
            i += 1

            for n in nums:
                heappush(heap, curr * n)

        return result


sol = Solution()
print(sol.solve(2, 3, 5, 5))  # [2, 3, 4, 5, 6]
print(sol.solve(3, 2, 7, 3))  # [2, 3, 4]
