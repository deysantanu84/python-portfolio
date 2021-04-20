# Given a string A of size N.
# Return the string A after reversing the string word by word.
# NOTE:
# A sequence of non-space characters constitutes a word.
# Your reversed string should not contain leading or trailing spaces,
# even if it is present in the input string.
# If there are multiple spaces between words, reduce them to a single space in the reversed string.
def reverseWord(M, startIndex, endIndex):
    while startIndex < endIndex:
        M[startIndex], M[endIndex] = M[endIndex], M[startIndex]
        startIndex += 1
        endIndex -= 1
    return M


def reverseString(A):
    A = list(A)
    reversedA = A[::-1]
    startWordIndex = 0
    for i in range(len(reversedA)):
        if reversedA[i] == ' ':
            if reversedA[i - 1] == ' ':
                reversedA.remove(A[i])
                continue
            endWordIndex = i - 1
            reversedA = reverseWord(reversedA, startWordIndex, endWordIndex)
            startWordIndex = i + 1
    reversedA = reverseWord(reversedA, startWordIndex, len(A) - 1)
    return ''.join(reversedA)


# print(reverseString("the sky is blue"))
# print(reverseString("this is ib"))
print(reverseString("       fwbpudnbrozzifml osdt ulc jsx kxorifrhubk ouhsuhf sswz qfho dqmy sn myq igjgip iwfcqq                 "))
