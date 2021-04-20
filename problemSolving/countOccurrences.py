# Find number of occurrences of bob in the string A consisting of lowercase english alphabets.
def countOccurrences(A):
    count = 0
    for i in range(len(A) - 2):
        if A[i: i + 3] == 'bob':
            count += 1
    return count


print(countOccurrences("abobc"))  # 1
print(countOccurrences("bobob"))  # 2
