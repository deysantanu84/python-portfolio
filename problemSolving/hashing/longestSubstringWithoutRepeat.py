# Given a string A, find the length of the longest substring without repeating characters.
# Note: Users are expected to solve in O(N) time complexity.
# 1 <= size(A) <= 10^6
# String consists of lowerCase,upperCase characters and digits are also present in the string A.
# Return an integer denoting the maximum possible length of substring without repeating characters.
# 1 <= size(A) <= 10^6
# String consists of lowerCase,upperCase characters and digits are also present in the string A.
def longestSubstringWithoutRepeat(A):
    indexDict = {}
    start = 0
    result = 0

    for i in range(len(A)):
        if A[i] in indexDict:
            start = max(start, indexDict[A[i]] + 1)
        result = max(result, i - start + 1)
        indexDict[A[i]] = i

    return result


print(longestSubstringWithoutRepeat("abcabcbb"))  # 3
print(longestSubstringWithoutRepeat("AaaA"))  # 2
