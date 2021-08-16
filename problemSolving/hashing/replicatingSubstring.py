# Given a string B, find if it is possible to re-order the characters of the string B
# so that it can be represented as a concatenation of A similar strings.
# Eg: B = aabb and A = 2, then it is possible to re-arrange the string as "abab"
# which is a concatenation of 2 similar strings "ab".
# If it is possible, return 1, else return -1.
# 1 <= Length of string B <= 1000
# 1 <= A <= 1000
# All the alphabets of S are lower case (a - z)
# Your function should return 1 if it is possible to re-arrange the characters of the string B
# so that it can be represented as a concatenation of A similar strings. If it is not, return -1.
from collections import Counter


def replicatingSubstring(A, B):
    counterDict = Counter(B)
    result = 1

    for i in counterDict.values():
        if i % A:
            result = -1
            break

    return result


print(replicatingSubstring(2, 'bbaabb'))  # 1
print(replicatingSubstring(1, 'bc'))  # 1
print(replicatingSubstring(5, 'abde'))  # -1
