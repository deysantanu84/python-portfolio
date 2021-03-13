# You have given a string A having Uppercase English letters.
# You have to find that how many times subsequence "AG" is there in the given string.
# NOTE: Return the answer modulo 10^9 + 7 as the answer can be very large.
def specialSubsequenceAG(A):
    count = 0
    countA = 0
    for i in range(len(A)):
        if A[i] == 'A':
            countA += 1
        if A[i] == 'G':
            count += countA
    return count % (10**9 + 7)


print(specialSubsequenceAG("ABCGAG"))
print(specialSubsequenceAG("GAB"))
