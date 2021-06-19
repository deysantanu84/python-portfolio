# You are given a function to_upper() consisting of a character array A.
# Convert each character of A into Uppercase character if it exists. If the Uppercase of a character does not exist, it remains unmodified.
# The lowercase letters from a to z is converted to uppercase letters from A to Z respectively.
# Return the uppercase version of the given character array.
def toUpper(A):
    N = len(A)
    for i in range(N):
        if 'a' <= A[i] <= 'z':
            A[i] = chr(ord(A[i]) - 32)
    return A


print(toUpper(['S', 'c', 'A', 'L', 'E', 'r', 'A', 'c', 'a', 'D', 'e', 'm', 'y']))
print(toUpper(['S', 'c', 'a', 'L', 'e', 'R', '#', '2', '0', '2', '0']))
