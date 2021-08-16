# Misha loves eating candies. She has given N boxes of Candies.
# She decides, every time she will choose a box having the minimum number of candies,
# eat half of the candies and put the remaining candies in the other box that has the minimum number of candies.
# Misha does not like a box if it has the number of candies greater than B so she won't eat from that box.
# Can you find how many candies she will eat?
# NOTE 1: If a box has an odd number of candies then Misha will eat floor(odd/2).
# NOTE 2: A same box will not be chosen again.
# 1 <= N <= 10^5
# 1 <= A[i] <= 10^5
# 1 <= B <= 10^6
# The first argument is A an Array of Integers, where A[i] is the number of candies in the ith box.
# The second argument is B, the maximum number of candies Misha like in a box.
# Return an Integer denoting number of candies Misha will eat.
from heapq import heapify, heappop, heapreplace


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        heapify(A)
        result = 0

        while len(A) > 1:
            curr = heappop(A)
            if curr > B:
                break

            if curr == 1:
                x = 0
                y = 1
            else:
                x = curr // 2
                y = curr - x

            result += x
            z = A[0] + y
            heapreplace(A, z)

        if A[0] <= B:
            result += (A[0]//2)

        return result


sol = Solution()
print(sol.solve([3, 2, 3], 4))  # 2
print(sol.solve([1, 2, 1], 2))  # 1
