# Given the array of strings A, you need to find the longest string S
# which is the prefix of ALL the strings in the array.
# Longest common prefix for a pair of strings S1 and S2 is the
# longest string S which is the prefix of both S1 and S2.
# For Example: longest common prefix of "abcdefgh" and "abcefgh" is "abc".
def longestCommonPrefix(A):
    result = ""
    A = sorted(A)
    N = len(A)
    N1 = len(A[0])
    N2 = len(A[N - 1])
    index1 = 0
    index2 = 0
    while index1 < N1 and index2 < N2:
        if A[0][index1] != A[N - 1][index2]:
            break
        result += (A[0][index1])
        index1 += 1
        index2 += 1
    return result


print(longestCommonPrefix(["abcdefgh", "aefghijk", "abcefgh"]))  # "a"
print(longestCommonPrefix(["abab", "ab", "abcd"]))  # "ab"
