# Given an array of integers, find two numbers such that they add up to a specific target number.
# The function twoSum should return indices of the two numbers such that they add up to the target,
# where index1 < index2.
# Please note that your returned answers (both index1 and index2) are not zero-based.
# Put both these numbers in order in an array and return the array from your function
# (Looking at the function signature will make things clearer ).
# Note that, if no pair exists, return empty list.
# If multiple solutions exist, output the one where index2 is minimum.
# If there are multiple solutions with the minimum index2, choose the one with minimum index1 out of them.
# Input: [2, 7, 11, 15], target=9
# Output: index1 = 1, index2 = 2
import sys
INT_MAX = sys.maxsize - 1


class Solution:
    def __init__(self, intTuple, targetSum):
        self.intTuple = intTuple
        self.targetSum = targetSum

    # @param A: tuple of integers
    # @param B: integer
    # @return a list of integers
    def twoSum(self):
        minIndex = 0
        minInnerIndex = 0
        for index in range(len(self.intTuple) - 1):
            for innerIndex in range(index + 1, len(self.intTuple)):
                if self.intTuple[index] + self.intTuple[innerIndex] == self.targetSum:
                    if minIndex and minInnerIndex:
                        if minInnerIndex > innerIndex + 1:
                            minIndex = index + 1
                            minInnerIndex = innerIndex + 1
                        elif minInnerIndex == innerIndex + 1:
                            if minIndex > index + 1:
                                minIndex = index + 1
                                minInnerIndex = innerIndex + 1
                    else:
                        minIndex = index + 1
                        minInnerIndex = innerIndex + 1

        if minIndex and minInnerIndex:
            return [minIndex, minInnerIndex]
        else:
            return []


def twoSum2(A, B):
    twoSumDict = {}
    for i in range(len(A)):
        if B - A[i] in A:
            if A[i] not in twoSumDict.keys():
                index1 = i + 1
                index2 = A.index(B - A[i]) + 1
                if index1 == index2:
                    if A.count(A[i]) > 1:
                        index2 = [j for j, entry in enumerate(A) if entry == (B - A[i])][1] + 1
                        result = sorted([index1, index2])
                        twoSumDict[A[i]] = result
                    else:
                        twoSumDict[A[i]] = None
                else:
                    result = sorted([index1, index2])
                    twoSumDict[A[i]] = result
        else:
            twoSumDict[A[i]] = None

    # print(twoSumDict)
    result = []
    minIndex1 = INT_MAX
    minIndex2 = INT_MAX
    for key, value in twoSumDict.items():
        if value is not None:
            currIndex1 = value[0]
            currIndex2 = value[1]
            if currIndex2 < minIndex2:
                minIndex2 = currIndex2
                result = value
            elif currIndex2 == minIndex2:
                if currIndex1 < minIndex1:
                    minIndex1 = currIndex1
                    result = value
    return result


def twoSum(A, B):
    result = []
    twoSumDict = {}
    for i in range(len(A)):
        if B - A[i] in twoSumDict.keys():
            return sorted([i + 1, twoSumDict[B - A[i]]])
        elif A[i] not in twoSumDict.keys():
            twoSumDict[A[i]] = i + 1
    return result


print(twoSum([0, 8, -3, -1, 7, 9, -1, 8, -2, 2, -8, -6, -7, -4, -6, -1, -6, 6, 8, -10, -6, 4, -8, 7, 6, -4, -4, -10, -6, 5, -8, -1, 10, 6, 6, -3, -3, -7, -8, -7, 4, -7, 1, -10, 5], 2))  # [1, 10]
print(twoSum([-7, -6, 7, 10, -1, -9, -8, 7, -5, -4, -4, 1, 6, 5, 7, 1, 3, -2, 9, -8, -6, -9, -4, -5], -2))  # [3, 6]
print(twoSum([1, 1, 1], 2))  # [1, 2]
print(twoSum([-10, -10, -10], -5))  # []
print(twoSum([2, 7, 11, 15], 9))  # [1, 2]
print(twoSum([4, 7, -4, 2, 2, 2, 3, -5, -3, 9, -4, 9, -7, 7, -1, 9, 9, 4, 1, -4, -2, 3, -3, -5, 4, -7, 7, 9, -4, 4, -8], -3))  # [4, 8]
