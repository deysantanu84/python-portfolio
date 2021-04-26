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
def replicatingSubstring(A, B):
    N = len(B)
    freqDict = {}

    for i in range(N):
        if B[i] in freqDict.keys():
            freqDict[B[i]] += 1
        else:
            freqDict[B[i]] = 1

    repeatingString = ''

    for i in range(26):
        if i in freqDict.keys() and freqDict[i] != 0:
            if freqDict[i] % A:
                return -1

            else:
                for j in range(freqDict[i] // A):
                    repeatingString += i
                    print(repeatingString)
    return 1


print(replicatingSubstring(2, 'bbaabb'))  # 1
# print(replicatingSubstring(1, 'bc'))  # 1
