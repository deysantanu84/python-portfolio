# Given a binary string A. It is allowed to do at most one swap between any 0 and 1.
# Find and return the length of the longest consecutive 1’s that can be achieved.
def longestConsecutiveOnes(A):
    result = 0
    left = []
    right = []
    count = 0
    for i in range(len(A) + 1):
        left.append(0)
        right.append(0)

    for i in range(len(A)):
        if A[i] == '1':
            count += 1
        else:
            count = 0
        left[i + 1] = count
    print(left)

    count = 0
    for i in range(len(A) - 1, -1, -1):
        if A[i] == '1':
            count += 1
        else:
            count = 0
        right[i] = count
    print(right)

    totalOnes = 0
    for i in range(len(A)):
        if A[i] == '1':
            totalOnes += 1

    for i in range(len(A)):
        if A[i] == '0':
            leftLength = left[i]
            rightLength = right[i+1]
            if leftLength + rightLength < totalOnes:
                result = max(result, leftLength + rightLength + 1)
            else:
                result = max(result, leftLength + rightLength)

    if '0' not in A:
        result = len(A)

    return result


# print(longestConsecutiveOnes("111000"))
# print(longestConsecutiveOnes("111011101"))
# print(longestConsecutiveOnes("11110011101"))
print(longestConsecutiveOnes("1111"))
