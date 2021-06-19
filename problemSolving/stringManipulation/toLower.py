# You are given a function to_lower() consisting of a character array A.
# Convert each character of A into lowercase character if it exists.
# If the lowercase of a character does not exist, it remains unmodified.
# The uppercase letters from A to Z is converted to lowercase letters from a to z respectively.
# Return the lowercase version of the given character array.
def toLower(A):
    N = len(A)
    for i in range(N):
        if 'A' <= A[i] <= 'Z':
            A[i] = chr(ord(A[i]) + 32)
    return A


print(toLower(['S', 'c', 'A', 'l', 'e', 'r', 'A', 'c', 'a', 'D', 'e', 'm', 'y']))
print(toLower(['S', 'c', 'a', 'L', 'e', 'r', '#', '2', '0', '2', '0']))
