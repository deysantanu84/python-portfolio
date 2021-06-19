# Given a string A of size N.
# Return the string A after reversing the string word by word.
# NOTE:
# A sequence of non-space characters constitutes a word.
# Your reversed string should not contain leading or trailing spaces,
# even if it is present in the input string.
# If there are multiple spaces between words, reduce them to a single space in the reversed string.
def reverseString(A):
    return " ".join(A.split()[::-1])


print(reverseString("the sky is blue"))
print(reverseString("this is ib"))
print(reverseString("       fwbpudnbrozzifml osdt ulc jsx kxorifrhubk ouhsuhf sswz qfho dqmy sn myq igjgip iwfcqq                 "))
