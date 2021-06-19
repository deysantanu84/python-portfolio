# Given a string A of size N consisting only of lowercase alphabets.
# The only operation allowed is to insert characters in the beginning of the string.
# Find and return how many minimum characters are needed to be
# inserted to make the string a palindrome string.
# 1 <= N <= 10^6
def computeLpsArray(A):
    N = len(A)
    lps = [-1] * N

    length = 0
    lps[0] = 0

    i = 1
    while i < N:
        if A[i] == A[length]:
            length += 1
            lps[i] = length
            i += 1

        else:
            if length != 0:
                length = lps[length - 1]

            else:
                lps[i] = 0
                i += 1

    return lps


def makeStringPalindrome(A):
    reverse = A[::-1]

    concat = A + "$" + reverse

    lps = computeLpsArray(concat)

    return len(A) - lps[-1]


print(makeStringPalindrome("abc"))  # 2
print(makeStringPalindrome("bb"))  # 0
