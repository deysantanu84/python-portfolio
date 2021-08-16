# Given 2 strings A and B of size N and M respectively consisting of lowercase alphabets, find the lexicographically
# smallest string that can be formed by concatenating non empty prefixes of A and B (in that order).
# Note: The answer string has to start with a non empty prefix of string A followed by a non empty prefix of string B.
# 1 <= N, M <= 100000
# First argument is a string A of size N.
# Second argument is a string B of size M.
# Return a string denoting Lexicographically smallest string that can be formed by
# concatenating non empty prefixes of A and B (in that order).
class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def smallestPrefix(self, A, B):
        N = len(A)
        result = [A[0]]

        for i in range(1, N):
            if ord(A[i]) < ord(B[0]):
                result.append(A[i])

            else:
                break

        result.append(B[0])
        return ''.join(result)


sol = Solution()
print(sol.smallestPrefix("abba", "cdd"))  # "abbac"
print(sol.smallestPrefix("acd", "bay"))  # "ab"
