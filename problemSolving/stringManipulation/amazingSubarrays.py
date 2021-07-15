# You are given a string S, and you have to find all the amazing substrings of S.
# Amazing Substring is one that starts with a vowel (a, e, i, o, u, A, E, I, O, U).
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
    result = 0
    for i in range(N):
        if isVowel(A[i]):
            result += N - i

    return result % 10003


print(amazingSubstrings('ABEC'))  # 6
print(amazingSubstrings("AzZGBauYuTknYjjWEEbLvqMQwnoSgXKBdHKEVpeoxYNNtBfrxQrPauttMzjKFayKwMeuChjzCocgAHfAmPCatOqarzLuabyTnxoheeocVshfERNssVPfRyPmwvOVGbzNAuvryYNWwIeyZLMlLbkcFFJRHjEIgIwOThRJJFpLbunVrbhAYsMtdsKslLAGElwrZjvZweIytMpPEYVmktQeNleNROcTjrNxXeHvOMMTMfqZHTUjetojHFzZwOekfAILYISANxeJFRNgeZDKoOTddXqxduPIjGXsRSSkgIqKMeSqlQwAKtdrkvHLgmKleNAPEztGMPmZzUuCImLAhzUnXmsVzFvJUTeIKleuRnMPNAPWJYAZLXgzTBPmkXVShbBSlIAJSeFgvRFvcoqfVFgHUefxUxuYFCfUxbxlOslUhYRFXKmMmqDIQhhfXyGqUwGMSYeLLpEsKAhvFUzavDCOUgtmmNMnsvfmCdPWuWIjuUfZCBTrWnaDopbqXcjzSqRMpQWIBNnMcOQZjDkjPkxsuwENYQyjgSHFJrgSLnwbEInBfdeIfBbVuZZbBrblJgKHOmLZACLQkSRxxQJeUMPIQutraxFtrRcSeqAejOTSqaFGglQOoWPkcNOnLIgfclWNtjGQRVMlqCPUnUlOLbHfkzUyNAmTsswWtZjIGUBrLmRmstHgVcRUgWdQTCEPRzjPVTMJRJocYHftwoRzOSyQexjmceRHdqFdgNuGmGTUdXQaNwKmvOUzZPzGCBVcbVLgMoQrESbpVGteVVntOwEWxXsZnSAoIfBSsWVhDFBuDTkcrnsPdmmSHymouxHlcgtjgKUAPznxsIRUjDFsrjadJjEtPaWTVBHpatqYeSgrpWJDOGfgIGQPcTIXVsCVyCfKMpcXWGkvwuRuTmvCbNMLeUkZrEpYZdlKAgFELfwCCbZCYBcXhfUrsIHfdwhYyxHKAMYMERwlyRtxObDoxBhjXmynYkmkYZrkzlCuvrhW"))  # 2099
