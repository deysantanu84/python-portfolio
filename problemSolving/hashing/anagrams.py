# Given an array A of N strings, return all groups of strings that are anagrams.
# Represent a group by a list of integers representing the index(1-based) in the original list.
# Look at the sample case for clarification.
# NOTE: Anagram : a word, phrase, or name formed by rearranging the letters of another,
# such as 'spar', formed from 'rasp'.
# 1 <= N <= 10^4
# 1 <= |A[i]| <= 10^4
# Each string consists only of lowercase characters.
# Sum of length of all the strings doesn't exceed 10^7
# Return a two-dimensional array where each row describes a group.
# Note:
# Ordering of the result :
# You should not change the relative ordering of the strings within the group
# suppose within a group containing A[i] and A[j], A[i] comes before A[j] if i < j.
def anagrams(A):
    wordDict = {}
    result = []

    for index in range(len(A)):
        sortedWord = ''.join(sorted(A[index]))

        if sortedWord in wordDict:
            wordDict[sortedWord].append(index + 1)

        else:
            wordDict[sortedWord] = [index + 1]

    for value in wordDict.values():
        result.append(value)

    return result


print(anagrams(['cat', 'dog', 'god', 'tca']))  # [[1, 4], [2, 3]]
print(anagrams(['rat', 'tar', 'art']))  # [[1, 2, 3]]
