# Given two array of integers A and B,
# Sort A in such a way that the relative order among the elements
# will be the same as those are in B. For the elements not present in B,
# append them at last in sorted order.
# Return the array A after sorting from the above method.
# NOTE: Elements of B are unique.
# 1 <= length of the array A <= 100000
# 1 <= length of the array B <= 100000
# -10^9 <= A[i] <= 10^9
def sortArrayInGivenOrder(A, B):
    result = []
    freqDict = {}

    for item in A:
        if item in freqDict.keys():
            freqDict[item] += 1
        else:
            freqDict[item] = 1

    for item in B:
        if item in A:
            result.extend([item] * freqDict[item])
            freqDict[item] = 0

    temp = []
    for item in freqDict.keys():
        if freqDict[item] != 0:
            temp.append(item)
    temp.sort()

    for item in temp:
        result.extend([item] * freqDict[item])

    return result


print(sortArrayInGivenOrder([1, 2, 3, 4, 5], [5, 4, 2]))  # [5, 4, 2, 1, 3]
print(sortArrayInGivenOrder([5, 17, 100, 11], [1, 100]))  # [100, 5, 11, 17]
