# Akash likes playing with strings. One day he thought of
# applying following operations on the string in the given order:
# Concatenate the string with itself.
# Delete all the uppercase letters.
# Replace each vowel with '#'.
# You are given a string A of size N consisting of lowercase and uppercase alphabets.
# Return the resultant string after applying the above operations.
# NOTE: 'a' , 'e' , 'i' , 'o' , 'u' are defined as vowels.
# 1<=N<=100000
# A="AbcaZeoB"
# Output: "bc###bc###"
import re


def stringOperations(A):
    A += A
    A = re.sub(r'[A-Z]', '', A)
    for i in A:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            A = A.replace(i, '#')
    return A


print(stringOperations("AbcaZeoB"))  # "bc###bc###"
