# Given two strings A and B. Find the longest common subsequence
# ( A sequence which does not need to be contiguous), which is common in both the strings.
# You need to return the length of such longest common subsequence.
# 1 <= Length of A, B <= 1005
# First argument is a string A.
# Second argument is a string B.
# Return an integer denoting the length of the longest common subsequence.
class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        M = len(A)
        N = len(B)
        resultMatrix = [[0 for _ in range(N + 1)] for _ in range(M + 1)]

        for row in range(1, M + 1):
            for col in range(1, N + 1):
                if A[row - 1] == B[col - 1]:
                    resultMatrix[row][col] = 1 + resultMatrix[row - 1][col - 1]

                else:
                    resultMatrix[row][col] = max(resultMatrix[row][col - 1],
                                                 resultMatrix[row - 1][col])

        return resultMatrix[M][N]


sol = Solution()
print(sol.solve("abbcdgf", "bbadcgf"))  # 5
print(sol.solve("aaaaaa", "ababab"))  # 3
