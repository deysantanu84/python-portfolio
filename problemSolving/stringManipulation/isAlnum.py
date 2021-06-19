# You are given a function isalpha() consisting of a character array A.
# Return 1 if all the characters of a character array are alphanumeric (a-z, A-Z and 0-9), else return 0.
def isAlnum(A):
    N = len(A)
    for i in range(N):
        if ord(A[i]) not in range(48, 58) \
                and ord(A[i]) not in range(65, 91) \
                and ord(A[i]) not in range(97, 123):
            return 0
    return 1


print(isAlnum(['S', 'c', 'a', 'l', 'e', 'r', 'A', 'c', 'a', 'd', 'e', 'm', 'y', '2', '0', '2', '0']))
print(isAlnum(['S', 'c', 'a', 'l', 'e', 'r', '#', '2', '0', '2', '0']))
