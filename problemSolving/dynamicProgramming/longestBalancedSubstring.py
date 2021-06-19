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
        invalidOpenBraces = 0
        invalidCloseBraces = 0

        for index in range(N):
            if A[index] == '(':
                invalidOpenBraces += 1

            else:
                if invalidOpenBraces == 0:
                    invalidCloseBraces += 1
                else:
                    invalidOpenBraces -= 1

        return N - (invalidOpenBraces + invalidCloseBraces)


sol = Solution()
print(sol.LBSlength("[()]"))  # 4
print(sol.LBSlength("[(])"))  # 0
