# Given an array A of both positive and negative integers.
# Your task is to compute sum of minimum and maximum elements of all sub-array of size B.
# NOTE: Since the answer can be very large, you are required to return the sum modulo 10^9 + 7.
# 1 <= size of array A <= 10^5
# -10^9 <= A[i] <= 10^9
# 1 <= B <= size of array
# The first argument denotes the integer array A.
# The second argument denotes the value B
# Return an integer that denotes the required value.
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        result = 0
        N = len(A)
        increasingQueue = []
        decreasingQueue = []

        for i in range(B):
            while len(increasingQueue) and A[increasingQueue[-1]] >= A[i]:
                increasingQueue.pop()

            while len(decreasingQueue) and A[decreasingQueue[-1]] <= A[i]:
                decreasingQueue.pop()

            decreasingQueue.append(i)
            increasingQueue.append(i)

        for i in range(B, N):
            result = (result % (10**9 + 7) + A[increasingQueue[0]] + A[decreasingQueue[0]]) % (10**9 + 7)

            while len(increasingQueue) and increasingQueue[0] <= i - B:
                increasingQueue.pop(0)

            while len(decreasingQueue) and decreasingQueue[0] <= i - B:
                decreasingQueue.pop(0)

            while len(increasingQueue) and A[increasingQueue[-1]] >= A[i]:
                increasingQueue.pop()

            while len(decreasingQueue) and A[decreasingQueue[-1]] <= A[i]:
                decreasingQueue.pop()

            decreasingQueue.append(i)
            increasingQueue.append(i)

        result = result % (10**9 + 7) + A[increasingQueue[0]] + A[decreasingQueue[0]] % (10**9 + 7)

        return result % (10**9 + 7)


sol = Solution()
print(sol.solve([2, 5, -1, 7, -3, -1, -2], 4))  # 18
print(sol.solve([2, -1, 3], 2))  # 3
