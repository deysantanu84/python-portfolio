# Given a string A of size N consisting of lowercase alphabets.
# You can change at most B characters in the given string to any other lowercase alphabet
# such that the number of distinct characters in the string is minimized.
# Find the minimum number of distinct characters in the resulting string.
# A = "abcabbccd"
# B = 3
# Output: 2
# We can change both 'a' and one 'd' into 'b'.So the new string becomes "bbcbbbccb".
# So the minimum number of distinct character will be 2.
def changeCharacter(A, B):
    charCount = {}
    for char in A:
        if char not in charCount:
            charCount[char] = 0
        charCount[char] += 1

    counts = sorted(charCount.values())
    result = len(counts)

    for i in range(len(counts) - 1):
        if counts[i] <= B:
            B -= counts[i]
            result -= 1

        else:
            break

    return result


print(changeCharacter("abcabbccd", 3))  # 2
