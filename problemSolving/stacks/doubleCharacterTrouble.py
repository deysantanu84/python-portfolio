# You are given a string A.
# An operation on the string is defined as follows:
# Remove the first occurrence of same consecutive characters. eg for a string "abbcd",
# the first occurrence of same consecutive characters is "bb".
# Therefore the string after this operation will be "acd".
# Keep performing this operation on the string until there are no more occurrences of
# same consecutive characters and return the final string.
# 1 <= |A| <= 100000
def doubleCharacterTrouble(A):
    stack = []

    for ch in A:
        stack.append(ch)
        if len(stack) > 1 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()

    return "".join(stack)


print(doubleCharacterTrouble("abccbc"))  # "ac"
print(doubleCharacterTrouble("ab"))  # "ab"
