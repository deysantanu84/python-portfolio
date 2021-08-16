# Given a string A of lowercase English alphabets. Rearrange the characters of the given string A
# such that there is no boring substring in A.
# A boring substring has the following properties:
# Its length is 2.
# Both the characters are consecutive, for example - "ab", "cd", "dc", "zy" etc.
# (If the first character is C then the next character can be either (C+1) or (C-1)).
# Return 1 if it possible to rearrange the letters of A such that there are no boring substring in A, else return 0.
# 1 <= |A| <= 10^5
# The only argument given is string A.
# Return 1 if it possible to rearrange the letters of A such that there are no boring substring in A, else return 0.
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        result = 0
        evenChars = []
        oddChars = []

        for char in A:
            if ord(char) % 2 == 0:
                evenChars.append(char)

            else:
                oddChars.append(char)

        if not len(evenChars) or not len(oddChars):
            return 1

        if abs(ord(min(evenChars)) - ord(max(oddChars))) != 1 \
                or abs(ord(max(evenChars)) - ord(min(oddChars))) != 1:
            result = 1

        return result


sol = Solution()
print(sol.solve("abcd"))  # 1
print(sol.solve("aab"))  # 0
