# Implement wildcard pattern matching with support for ' ? ' and ' * ' for strings A and B.
# ' ? ' : Matches any single character.
# ' * ' : Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).
# 1 <= length(A), length(B) <= 10^4
# The first argument of input contains a string A.
# The second argument of input contains a string B.
# Return 1 if the patterns match else return 0.
class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def isMatch(self, A, B):
        if len(B) - B.count('*') > len(A):
            return 0

        resultList = [True] + [False] * len(A)

        for entry in B:
            if entry == '*':
                for x in range(1, len(A) + 1):
                    resultList[x] = resultList[x - 1] or resultList[x]

            else:
                for x in range(len(A) - 1, -1, -1):
                    resultList[x + 1] = resultList[x] and (entry == A[x] or entry == '?')

                resultList[0] = resultList[0] and entry == '*'

        if resultList[-1]:
            return 1
        else:
            return 0


sol = Solution()
print(sol.isMatch("aaa", "a*"))  # 1
print(sol.isMatch("acz", "a?a"))  # 0
print(sol.isMatch("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                  "a**************************************************************************************"))  # 1
