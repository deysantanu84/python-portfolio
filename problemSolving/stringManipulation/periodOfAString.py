# Given a string A of length N consisting of lowercase alphabets. Find the period of the string.
# Period of the string is the minimum value of k (k >= 1), that satisfies A[i] = A[i % k] for all valid i.
# 1 <= N <= 10^6
# First and only argument is a string A of length N.
# Return an integer, denoting the period of the string.
class Solution:
    def util(self, string, M, lps):
        length = 0
        i = 1
        lps[0] = 0

        while i < M:
            if string[i] == string[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length:
                    length = lps[length - 1]

                else:
                    lps[i] = 0
                    i += 1

    # @param A : string
    # @return an integer
    def solve(self, A):
        N = len(A)
        lps = [0] * N

        self.util(A, N, lps)
        length = lps[N - 1]

        return N - length


sol = Solution()
print(sol.solve("abababab"))  # 2
print(sol.solve("aaaa"))  # 1
print(sol.solve("umeaylnlfdumeaylnlfdumeaylnlfd"))  # 10
print(sol.solve("abcaabcaab"))  # 4
