# Shaggy has an array A consisting of N elements.
# We call a pair of distinct indices in that array as a special pair
# if elements at that index in the array are equal.
# Shaggy wants you to find a special pair such that distance between that pair is minimum.
# Distance between two indices is defined as |i-j|.
# If there is no special pair in the array then return -1.
# 1 <= |A| <= 10^5
# Return one integer corresponding to the minimum possible distance between a special pair.
import sys
INT_MAX = sys.maxsize - 1


def minimumDistance(A):
    currMin = INT_MAX
    distanceDict = {}

    for i in range(len(A)):
        if A[i] not in distanceDict:
            distanceDict[A[i]] = i
        else:
            if abs(i - distanceDict[A[i]]) < currMin:
                currMin = abs(i - distanceDict[A[i]])

    if currMin < INT_MAX:
        return currMin
    else:
        return -1


print(minimumDistance([7, 1, 3, 4, 1, 7]))  # 3
print(minimumDistance([1, 1]))  # 1
