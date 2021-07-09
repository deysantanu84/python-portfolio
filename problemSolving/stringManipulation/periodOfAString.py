# Given a string A of length N consisting of lowercase alphabets. Find the period of the string.
# Period of the string is the minimum value of k (k >= 1), that satisfies A[i] = A[i % k] for all valid i.
# 1 <= N <= 10^6
# First and only argument is a string A of length N.
# Return an integer, denoting the period of the string.
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        i = (A + A[::-1]).find(A, 1, -1)
        print(i)
        return None if i == -1 else len(A[:i])


sol = Solution()
print(sol.solve("abababab"))  # 2
print(sol.solve("aaaa"))  # 1
print(sol.solve("umeaylnlfdumeaylnlfdumeaylnlfd"))  # 10
print(sol.solve("abcaabcaab"))  # 4
