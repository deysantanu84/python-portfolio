# Given a string A made up of multiple brackets of type "[]" , "()" and "{}"
# find the length of the longest substring which forms a balanced string .
# Conditions for a string to be balanced :
# Blank string is balanced ( However blank string will not be provided as a test case ).
# If B is balanced : (B) , [B] and {B} are also balanced.
# If B1 and B2 are balanced then B1B2 i.e the string formed by concatenating B1 and B2 is also balanced.
# 0 <= |A| <= 10^6
# First and only argument is an string A.
# Return an single integer denoting the length of the longest balanced substring.
class Solution:
    # @param A : string
    # @return an integer
    def LBSlength(self, A):
        N = len(A)
        if N < 2:
            return 0

        result = 0
        longest = [0 for _ in range(N)]

        for i in range(1, N):
            if A[i] == ')' or A[i] == ']' or A[i] == '}':
                if ((A[i] == ']' and A[i - 1] == '[') or
                        (A[i] == '}' and A[i - 1] == '{') or
                        (A[i] == ')' and A[i - 1] == '(')):
                    longest[i] = longest[i - 2] + 2
                    result = max(result, longest[i])

                else:
                    if (((i - longest[i - 1] - 1) >= 0) and
                            ((A[i] == ']' and A[i - longest[i - 1] - 1] == '[') or
                             (A[i] == '}' and A[i - longest[i - 1] - 1] == '{') or
                             (A[i] == ')' and A[i - longest[i - 1] - 1] == '('))):

                        if (i - longest[i - 1] - 2) >= 0:
                            longest[i] = longest[i-1] + 2 + longest[i-longest[i-1] - 2]
                        else:
                            longest[i] = longest[i-1] + 2

                        result = max(result, longest[i])

        return result


sol = Solution()
print(sol.LBSlength("[()]"))  # 4
print(sol.LBSlength("[(])"))  # 0
print(sol.LBSlength("([[]]()}[]([[]]([[]]))["))  # 14
