# You are given an array A of N integers and three integers B, C, and D.
# You have to find the maximum value of A[i]*B + A[j]*C + A[k]*D, where 1 <= i <= j <= k <= N.
# 1 <= N <= 10^5
# -10000 <= A[i], B, C, D <= 10000
# First argument is an array A
# Second argument is an integer B
# Third argument is an integer C
# Fourth argument is an integer D
# Return an Integer S, i.e maximum value of (A[i] * B + A[j] * C + A[k] * D), where 1 <= i <= j <= k <= N.
import sys
INT_MIN = -sys.maxsize


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @return an integer
    def solve(self, A, B, C, D):
        N = len(A)
        result = INT_MIN

        leftMaxList = [0] * N
        leftMaxList[0] = B * A[0]

        for index in range(1, N):
            leftMaxList[index] = max(leftMaxList[index - 1], B * A[index])

        rightMaxList = [0] * N
        rightMaxList[N - 1] = D * A[N - 1]

        for index in range(N - 2, -1, -1):
            rightMaxList[index] = max(rightMaxList[index + 1], D * A[index])

        for index in range(N):
            result = max(result, leftMaxList[index] + C * A[index] + rightMaxList[index])

        return result


sol = Solution()
print(sol.solve([1, 5, -3, 4, -2], 2, 1, -1))  # 18
print(sol.solve([3, 2, 1], 1, -10, 3))  # -4
