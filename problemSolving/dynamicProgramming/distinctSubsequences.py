# Given two sequences A and B, count number of unique ways in sequence A,
# to form a subsequence that is identical to the sequence B.
# Subsequence : A subsequence of a string is a new string which is formed from
# the original string by deleting some (can be none) of the characters without
# disturbing the relative positions of the remaining characters.
# (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).
# 1 <= length(A), length(B) <= 700
# The first argument of input contains a string A.
# The second argument of input contains a string B.
# Return an integer representing the answer as described in the problem statement.
class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def numDistinct(self, A, B):
        M = len(A)
        N = len(B)
        resultGrid = [[0 for _ in range(M + 1)] for _ in range((N + 1))]

        for i in range(M + 1):
            resultGrid[0][i] = 1

        for i in range(1, M + 1):
            for j in range(1, N + 1):
                resultGrid[j][i] = resultGrid[j][i - 1]

                if A[i - 1] == B[j - 1]:
                    resultGrid[j][i] += resultGrid[j - 1][i - 1]

        return resultGrid[-1][-1]


sol = Solution()
print(sol.numDistinct("abc", "abc"))  # 1
print(sol.numDistinct("rabbbit", "rabbit"))  # 3
