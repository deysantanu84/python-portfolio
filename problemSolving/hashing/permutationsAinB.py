# You are given two strings A and B of size N and M respectively.
# You have to find the count of all permutations of A present in B as a substring.
# You can assume a string will have only lowercase letters.
# 1 <= N < M <= 10^5
# A = "abc", B = "abcbacabc" ---> 5
# A = "aca", B = "acaa" ---> 2
def isMatch(P, Q):
    for i in range(256):
        if P[i] != Q[i]:
            return False
    return True


def substringPermutations(A, B):
    count = 0
    M = len(A)
    N = len(B)
    countAList = [0] * 256
    countBList = [0] * 256
    for i in range(M):
        countAList[ord(A[i])] += 1
        countBList[ord(B[i])] += 1
    for i in range(M, N):
        if isMatch(countAList, countBList):
            count += 1
        countBList[ord(B[i])] += 1
        countBList[ord(B[i - M])] -= 1
    if isMatch(countAList, countBList):
        count += 1
    return count


def permutationsOfAInB(A, B):
    N = len(A)
    M = len(B)
    count = 0

    hashSumA = 0
    hashSumB = 0

    if N > M:
        return 0

    for i in range(N):
        hashSumB += hash(B[i])
        hashSumA += hash(A[i])

    if hashSumB == hashSumA:
        count += 1

    for i in range(N, M):
        hashSumB += hash(B[i]) - hash(B[i - N])

        if hashSumB == hashSumA:
            count += 1

    return count


# print(substringPermutations("abc", "abcbacabc"))  # 5
print(permutationsOfAInB("abc", "abcbacabc"))  # 5
# print(substringPermutations("aca", "acaa"))  # 2
print(permutationsOfAInB("aca", "acaa"))  # 2
