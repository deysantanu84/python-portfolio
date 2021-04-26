# Given a string A and a string B, find the window with minimum length in A
# which will contain all the characters in B in linear time complexity.
# Note that when the count of a character c in B is x,
# then the count of c in minimum window in A should be at least x.
# Note:
# If there is no such window in A that covers all characters in B, return the empty string.
# If there are multiple such windows, return the first occurring minimum window
# ( with minimum start index )
# 1 <= size(A), size(B) <= 10^6
# Python3 program to find the smallest window
# containing all characters of a pattern.
def windowString(A, B):
    M = len(A)
    N = len(B)

    if M == 0 or N == 0 or N > M:
        return ""

    bDict = {}
    for ch in B:
        if ch in bDict:
            bDict[ch] += 1
        else:
            bDict[ch] = 1

    i = 0
    j = 0
    currMin = M + 1
    result = ""

    while i < M:
        if A[i] in bDict:
            if bDict[A[i]] > 0:
                N -= 1
            bDict[A[i]] -= 1

        while N == 0:
            if i - j + 1 < currMin:
                currMin = i - j + 1
                result = A[j: i + 1]

            if A[j] in bDict:
                bDict[A[j]] += 1

                if bDict[A[j]] > 0:
                    N += 1

            j += 1
        i += 1

    if currMin == M + 1:
        return ""

    return result


print(windowString("ADOBECODEBANC", "ABC"))  # "BANC"
print(windowString("Aa91b", "ab"))  # "a91b"
