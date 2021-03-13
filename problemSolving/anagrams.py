# Given an array A of N strings, return all groups of strings that are anagrams.
# Represent a group by a list of integers representing the index(1-based) in the original list.
# Look at the sample case for clarification.
# Return a two-dimensional array where each row describes a group
# NOTE: Anagram : a word, phrase, or name formed by rearranging the letters of another,
# such as 'spar', formed from 'rasp'.
# Ordering of the result : You should not change the relative ordering of the strings within the group
# suppose within a group containing A[i] and A[j], A[i] comes before A[j] if i < j.
# [cat, dog, god, tca] ---> [[1, 4], [2, 3]]
# [rat, tar, art] ---> [[1, 2, 3]]
def anagrams(A):
    result = []
    anagramsDict = {}
    for i in range(len(A)):
        key = ''.join(sorted(A[i]))
        if key not in anagramsDict:
            anagramsDict[key] = [i + 1]
        else:
            anagramsDict[key].append(i+1)

    for value in anagramsDict.values():
        result.append(value)

    return result


print(anagrams(['cat', 'dog', 'god', 'tca']))
print(anagrams(['rat', 'tar', 'art']))
