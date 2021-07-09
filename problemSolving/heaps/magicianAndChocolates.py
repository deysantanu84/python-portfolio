# Given N bags, each bag contains Bi chocolates. There is a kid and a magician. In one unit of time,
# kid chooses a random bag i, eats Bi chocolates, then the magician fills the ith bag with
# floor(Bi/2) chocolates.
# Find the maximum number of chocolates that kid can eat in A units of time.
# NOTE:
# floor() function returns the largest integer less than or equal to a given number.
# Return your answer modulo 10^9+7
# 1 <= N <= 100000
# 0 <= B[i] <= INT_MAX
# 0 <= A <= 10^5
# First argument is an integer A.
# Second argument is an integer array B of size N.
# Return an integer denoting the maximum number of chocolates that kid can eat in A units of time.
from heapq import heappop, heappush


class MaxHeap(int):
    def __lt__(self, val):
        return self > val


class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def nchoc(self, A, B):
        result = 0
        heap = []

        for item in B:
            heappush(heap, MaxHeap(item))

        for _ in range(A):
            temp = heappop(heap)
            result += temp
            heappush(heap, MaxHeap(temp // 2))

        return result % (10**9 + 7)


sol = Solution()
print(sol.nchoc(3, [6, 5]))  # 14
print(sol.nchoc(5, [2, 4, 6, 8, 10]))  # 33
