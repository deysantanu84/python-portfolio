# Given a string A, partition A such that every string of the partition is a palindrome.
# Return all possible palindrome partitioning of A.
# Ordering the results in the answer : Entry i will come before Entry j if :
# len(Entryi[0]) < len(Entryj[0]) OR
# (len(Entryi[0]) == len(Entryj[0]) AND len(Entryi[1]) < len(Entryj[1])) OR * * *
# (len(Entryi[0]) == len(Entryj[0]) AND ... len(Entryi[k] < len(Entryj[k]))
def partitions(S, partition, result):
    if not S:
        result.append(partition[::])
        return

    for i in range(1, len(S) + 1):
        prefix, postfix = S[:i], S[i:]

        if isPalindrome(prefix):
            partition.append(prefix)
            partitions(postfix, partition, result)
            partition.pop()


def isPalindrome(S):
    return S == S[::-1]


def palindromePartitioning(A):
    result = []
    partitions(A, [], result)
    return result

print(palindromePartitioning("aab"))
print(palindromePartitioning("a"))
