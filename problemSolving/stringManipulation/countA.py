# You are given a string A. Find the number of substrings that start and end with 'a'.
# 1 <= |A| <= 10^5
# String will have only lowercase English letters.
# TLE
def countA(A):
    N = len(A)
    count = 0

    for i in range(N):
        if A[i] == 'a':
            count += 1
            for j in range(i + 1, N):
                if A[j] == 'a':
                    count += 1

    return count


print(countA("aab"))  # 3
print(countA("bcbc"))  # 0
