# Given an array of integers A .
# value of a array = max(array) - min(array).
# Calculate and return the sum of values of all possible subarrays of A % 10^9+7.
# 1 <= |A| <= 100000
# 1 <= A[i] <= 1000000
# The first and only argument given is the integer array A.
# Return the sum of values of all possible subarrays of A % 10^9+7.
# TLE
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        result = 0
        N = len(A)

        for j in range(N):
            increasing = []
            decreasing = []
            for i in range(j, N):
                while len(increasing) and increasing[-1] >= A[i]:
                    increasing.pop()

                while len(decreasing) and decreasing[-1] <= A[i]:
                    decreasing.pop()

                decreasing.append(A[i])
                increasing.append(A[i])
                result += (decreasing[0] - increasing[0]) % (10**9 + 7)

        return result % (10**9 + 7)


sol = Solution()
print(sol.solve([1]))  # 0
print(sol.solve([4, 7, 3, 8]))  # 26
