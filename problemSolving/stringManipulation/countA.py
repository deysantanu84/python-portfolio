# You are given a string A. Find the number of substrings that start and end with 'a'.
# 1 <= |A| <= 10^5
# String will have only lowercase English letters.
def countAUtil(A, n, x, y):
    result = 0
    countX = 0

    for i in range(n):
        if A[i] == x:
            countX += 1

        if A[i] == y:
            result += countX

    return result


def countA(A):
    return countAUtil(A, len(A), 'a', 'a')


print(countA("aab"))  # 3
print(countA("bcbc"))  # 0
