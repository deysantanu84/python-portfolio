# Groot has a profound love for palindrome which is why he keeps fooling around with strings.
# A palindrome string is one that reads the same backward as well as forward.
# Given a string A of size N consisting of lowercase alphabets,
# he wants to know if it is possible to make the given string a palindrome
# by changing exactly one of its character.
def closestPalindrome(A):
    N = len(A)
    count = 0
    for i in range(N//2):
        if A[i] != A[N - i - 1]:
            count += 1
    if N % 2 and count == 0:
        count += 1
    if count == 1:
        return 'YES'
    else:
        return 'NO'


print(closestPalindrome('abba'))  # 'NO'
print(closestPalindrome('abbba'))  # 'YES'
print(closestPalindrome('adaddb'))  # 'NO'
print(closestPalindrome('abcca'))  # 'YES'
