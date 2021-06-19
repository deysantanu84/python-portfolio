# You are given a string S, and you have to find all the amazing substrings of S.
# Amazing Substring is one that starts with a vowel (a, e, i, o, u, A, E, I, O, U).
def amazingSubstrings2(A):
    vowels = 'aeiouAEIOU'
    substringList = []
    for index, entry in enumerate(A):
        for j in range(index + 1, len(A) + 1):
            if entry in vowels:
                substringList.append(A[index: j])
    return len(substringList) % 10003


def isVowel(P):
    return (P == 'a'
            or P == 'e'
            or P == 'i'
            or P == 'o'
            or P == 'u'
            or P == 'A'
            or P == 'E'
            or P == 'I'
            or P == 'O'
            or P == 'U')


def amazingSubstrings(A):
    N = len(A)
    countList = []
    for i in range(0, N + 1):
        countList.append(0)
    if isVowel(A[N - 1]):
        countList[N - 1] = 1
    for i in range(N - 2, -1, -1):
        if isVowel(A[i]):
            countList[i] = countList[i + 1] + 1
    count = 0
    for i in range(N):
        if isVowel(A[i]):
            count += countList[i + 1]
    return count


print(amazingSubstrings('ABEC'))
print(amazingSubstrings("AzZGBauYuTknYjjWEEbLvqMQwnoSgXKBdHKEVpeoxYNNtBfrxQrPauttMzjKFayKwMeuChjzCocgAHfAmPCatOqarzLuabyTnxoheeocVshfERNssVPfRyPmwvOVGbzNAuvryYNWwIeyZLMlLbkcFFJRHjEIgIwOThRJJFpLbunVrbhAYsMtdsKslLAGElwrZjvZweIytMpPEYVmktQeNleNROcTjrNxXeHvOMMTMfqZHTUjetojHFzZwOekfAILYISANxeJFRNgeZDKoOTddXqxduPIjGXsRSSkgIqKMeSqlQwAKtdrkvHLgmKleNAPEztGMPmZzUuCImLAhzUnXmsVzFvJUTeIKleuRnMPNAPWJYAZLXgzTBPmkXVShbBSlIAJSeFgvRFvcoqfVFgHUefxUxuYFCfUxbxlOslUhYRFXKmMmqDIQhhfXyGqUwGMSYeLLpEsKAhvFUzavDCOUgtmmNMnsvfmCdPWuWIjuUfZCBTrWnaDopbqXcjzSqRMpQWIBNnMcOQZjDkjPkxsuwENYQyjgSHFJrgSLnwbEInBfdeIfBbVuZZbBrblJgKHOmLZACLQkSRxxQJeUMPIQutraxFtrRcSeqAejOTSqaFGglQOoWPkcNOnLIgfclWNtjGQRVMlqCPUnUlOLbHfkzUyNAmTsswWtZjIGUBrLmRmstHgVcRUgWdQTCEPRzjPVTMJRJocYHftwoRzOSyQexjmceRHdqFdgNuGmGTUdXQaNwKmvOUzZPzGCBVcbVLgMoQrESbpVGteVVntOwEWxXsZnSAoIfBSsWVhDFBuDTkcrnsPdmmSHymouxHlcgtjgKUAPznxsIRUjDFsrjadJjEtPaWTVBHpatqYeSgrpWJDOGfgIGQPcTIXVsCVyCfKMpcXWGkvwuRuTmvCbNMLeUkZrEpYZdlKAgFELfwCCbZCYBcXhfUrsIHfdwhYyxHKAMYMERwlyRtxObDoxBhjXmynYkmkYZrkzlCuvrhW"))
