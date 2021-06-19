# Given a string A. Find the longest palindromic subsequence
# (A subsequence which does not need to be contiguous and is a palindrome).
# You need to return the length of longest palindromic subsequence.
# 1 <= length of(A) <= 10^3
# First and only integer is a string A.
# Return an integer denoting the length of longest palindromic subsequence.
class Solution:
    def util(self, x, y):
        N = len(x)
        resultGrid = [[-1] * (N + 1) for _ in range(N + 1)]

        for i in range(N + 1):
            for j in range(N + 1):
                if i == 0 or j == 0:
                    resultGrid[i][j] = 0

                elif x[i - 1] == y[j - 1]:
                    resultGrid[i][j] = 1 + resultGrid[i - 1][j - 1]

                else:
                    resultGrid[i][j] = max(resultGrid[i - 1][j], resultGrid[i][j - 1])

        return resultGrid[-1][-1]

    # @param A : string
    # @return an integer
    def solve(self, A):
        return self.util(A, A[::-1])


sol = Solution()
print(sol.solve("bebeeed"))  # 4
print(sol.solve("aedsead"))  # 5
