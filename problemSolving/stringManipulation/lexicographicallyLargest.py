# You are given a string S. You want to change it to the lexicographically
# largest possible string by changing some of its characters.
# But you can only use characters of the string T as a replacement for characters of S.
# Formally, find the lexicographically largest string you can form by replacing
# some(or none) of the characters of S by using only the characters of string T.
# Note: Each character of T can be used at the most once.
# Constraints:
# 1.   1 <= Length of S and T <= 50
# 2.   All the alphabets of S and T are lower case (a - z)
# Input: A string A containing S and T separated by "_" character. (See example below)
# Output: Lexicographically largest string P that can be formed by changing some or
# (none) characters of S using the characters of T.
# A : "abb_c"
# This implies S is "abb" and T is "c".
# Output: P = "cbb"
class Solution:
    def sortT(self, T):
        for i in range(len(T)):
            for j in range(i + 1, len(T)):
                if T[j] > T[i]:
                    T[i], T[j] = T[j], T[i]

    # @param A : string
    # @return a strings
    def getLargest(self, A):
        aSplit = A.split("_")
        S = list(aSplit[0])
        T = list(aSplit[1])
        self.sortT(T)

        for i in range(len(T)):
            for j in range(len(S)):
                if S[j] < T[i]:
                    S[j] = T[i]
                    T[i] = ''

        return ''.join(S)


sol = Solution()
print(sol.getLargest('abb_c'))  # 'cbb'
print(sol.getLargest('xyzab_cd'))  # 'xyzdc'
print(sol.getLargest('ittmcsvmoa_jktvvblefw'))  # 'wvvtlsvmok'
