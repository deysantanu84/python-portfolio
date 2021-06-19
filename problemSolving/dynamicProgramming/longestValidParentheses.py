# Given a string A containing just the characters '(' and ')'.
# Find the length of the longest valid (well-formed) parentheses substring.
# 1 <= length(A) <= 750000
# The only argument given is string A.
# Return the length of the longest valid (well-formed) parentheses substring.
class Solution:
    # @param A : string
    # @return an integer
    def longestValidParentheses(self, A):
        N = len(A)

        if N < 2:
            return 0

        resultList = [0 for _ in range(N)]
        if A[0:2] == '()':
            resultList[1] = 2

        else:
            resultList[1] = 0

        for i in range(2, N):
            if A[i] == ')':
                if A[i-1] == '(':
                    resultList[i] = resultList[i - 2] + 2

                else:
                    if i - resultList[i - 1] - 1 >= 0 and A[i - resultList[i - 1] - 1] == '(':
                        if i - resultList[i - 1] - 2 >= 0:
                            prefix = resultList[i - resultList[i - 1] - 2]

                        else:
                            prefix = 0

                        resultList[i] = prefix + resultList[i - 1] + 2

        return max(resultList)


sol = Solution()
print(sol.longestValidParentheses("(()"))  # 2
print(sol.longestValidParentheses(")()())"))  # 4
