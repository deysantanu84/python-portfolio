# Given an array of integers A and an integer B.
# We need to reverse the order of the first B elements of the array,
# leaving the other elements in the same relative order.
# NOTE: You are required to first insert elements into an auxiliary queue
# then perform Reversal of first B elements.
# 1 <= B <= length of the array <= 500000
# 1 <= A[i] <= 100000
# The argument given is the integer array A and an integer B.
# Return an array of integer after reversing the first B elements of A using queue.
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        for i in range(0, B // 2):
            temp = A[i]
            A[i] = A[B - i - 1]
            A[B - i - 1] = temp

        return A


sol = Solution()
print(sol.solve([1, 2, 3, 4, 5], 3))  # [3, 2, 1, 4, 5]
print(sol.solve([5, 17, 100, 11], 2))  # [17, 5, 100, 11]
