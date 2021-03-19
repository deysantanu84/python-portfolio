# In an alien language, surprisingly they also use english lowercase letters,
# but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.
# Given an array of words A of size N written in the alien language,
# and the order of the alphabet denoted by string B of size 26,
# return 1 if and only if the given words are sorted lexicographically in this alien language else return 0.
def isDictionary(A, B):
    orderDict = {}
    for index, entry in enumerate(B):
        orderDict[entry] = index
    for index in range(len(A) - 1):
        for index1 in range(min(len(A[index]), len(A[index + 1]))):
            if A[index][index1] != A[index + 1][index1]:
                if orderDict[A[index][index1]] > orderDict[A[index + 1][index1]]:
                    return 0
                break
        else:
            if len(A[index]) > len(A[index + 1]):
                return 0
    return 1


print(isDictionary(["hello", "scaler", "interviewbit"], "adhbcfegskjlponmirqtxwuvzy"))  # 1
print(isDictionary(["fine", "none", "no"], "qwertyuiopasdfghjklzxcvbnm"))  # 0
