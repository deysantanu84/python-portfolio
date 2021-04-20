# Given a string A, partition A such that every string of the partition is a palindrome.
# Return all possible palindrome partitioning of A.
# Ordering the results in the answer : Entry i will come before Entry j if :
# len(Entryi[0]) < len(Entryj[0]) OR
# (len(Entryi[0]) == len(Entryj[0]) AND len(Entryi[1]) < len(Entryj[1])) OR * * *
# (len(Entryi[0]) == len(Entryj[0]) AND ... len(Entryi[k] < len(Entryj[k]))
def isPalindrome(S):
    N = len(S)
    N -= 1
    for i in range(N):
        if S[i] != S[N]:
            return False
        N -= 1
    return True


def partitions(result, A, palindrome, index):
    length = len(A)
    S = ""
    current = palindrome[:]
    if index == 0:
        palindrome = []
    for i in range(index, length):
        S += A[i]
        if isPalindrome(S):
            palindrome.append(S)
            if i + 1 < length:
                partitions(result, A, palindrome[:], i + 1)
            else:
                result.append(palindrome)
            palindrome = current


def palindromePartitioning(A):
    result = []
    palindrome = []
    partitions(result, A, palindrome[:], 0)
    return result


print(palindromePartitioning("geeks"))
print(palindromePartitioning("aab"))
print(palindromePartitioning("a"))
