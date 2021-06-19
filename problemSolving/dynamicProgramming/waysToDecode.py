# A message containing letters from A-Z is being encoded to numbers using the following mapping:
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given an encoded message denoted by string A containing digits,
# determine the total number of ways to decode it modulo 10^9 + 7.
# 1 <= length(A) <= 10^5
# The first and the only argument is a string A.
# Return an integer, representing the number of ways to decode the string modulo 10^9 + 7..
class Solution:
    # @param A : string
    # @return an integer
    def numDecodings(self, A):
        decodeList = [1] * (len(A) + 1)
        if A[0] == "0":
            decodeList[1] = 0

        for i in range(2, len(A) + 1):
            if 1 <= int(A[i - 1]) <= 26:
                decodeList[i] = decodeList[i - 1]
            else:
                decodeList[i] = 0

            if 10 <= int(A[i - 2] + A[i - 1]) <= 26:
                decodeList[i] = (decodeList[i] + decodeList[i - 2]) % (10**9 + 7)

        return decodeList[-1]


sol = Solution()
print(sol.numDecodings("12"))  # 2
print(sol.numDecodings("8"))  # 1
