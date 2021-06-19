# You are given a function isalpha() consisting of a character array A.
# Return 1 if all the characters of the character array are alphabetical (a-z and A-Z), else return 0.
def isAlpha(A):
    N = len(A)
    for i in range(N):
        if ord(A[i]) not in range(65, 91) \
                and ord(A[i]) not in range(97, 123):
            return 0
    return 1


print(isAlpha(['S', 'c', 'a', 'l', 'e', 'r', 'A', 'c', 'a', 'd', 'e', 'm', 'y']))
print(isAlpha(['S', 'c', 'a', 'l', 'e', 'r', '#', '2', '0', '2', '0']))
