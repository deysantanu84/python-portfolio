# Given an integer array A of size N.
# You have to find the product of the 3 largest integers in array A from range 1 to i, where i goes from 1 to N.
# Return an array B where B[i] is the product of the largest 3 integers in range 1 to i in array A.
# If i < 3, then the integer at index i is -1.
# 1 <= N <= 10^5
# 0 <= A[i] <= 10^3
# First and only argument is an integer array A.
# Return an integer array B. B[i] denotes the product of the largest 3 integers in range 1 to i in array A.
from queue import PriorityQueue


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        N = len(A)
        result = []
        queue = PriorityQueue()

        for i in range(N):
            queue.put(-A[i])
            if queue.qsize() < 3:
                result.append(-1)
            else:
                x = queue.get()
                y = queue.get()
                z = queue.get()

                result.append(x * y * z * -1)

                queue.put(x)
                queue.put(y)
                queue.put(z)

        return result


sol = Solution()
print(sol.solve([1, 2, 3, 4, 5]))  # [-1, -1, 6, 24, 60]
print(sol.solve([10, 2, 13, 4]))  # [-1, -1, 260, 520]
