# Given a binary array A, find the maximum sequence of continuous 1's
# that can be formed by replacing at-most B zeroes.
# For this problem, return the indices of maximum continuous series of 1s in order.
# If there are multiple possible solutions, return the sequence which has the minimum start index.
# 0 <= B <= 10^5
# 1 <= size(A) <= 10^5
# A[i]==0 or A[i]==1
# First argument is an binary array A.
# Second argument is an integer B.
# Return an array of integers denoting the indices(0-based) of 1's in the maximum continuous series.
# Input 1:
#  A = [1 1 0 1 1 0 0 1 1 1 ]
#  B = 1
# Input 2:
#  A = [1, 0, 0, 0, 1, 0, 1]
#  B = 2
# Output 1:
#  [0, 1, 2, 3, 4]
# Output 2:
#  [3, 4, 5, 6]
# Explanation 1:
#  Flipping 0 present at index 2 gives us the longest continuous series of 1's i.e subarray [0:4].
# Explanation 2:
#  Flipping 0 present at index 3 and index 5 gives us the longest
#  continuous series of 1's i.e subarray [3:6].
def maxContinuousSeriesOf1s(A, B):
    temp = 0
    result = []
    flipCount = 0
    currMax = 0
    left = 0
    for right in range(len(A)):
        if A[right] == 0:
            flipCount += 1
        while flipCount > B:
            if A[temp] == 0:
                flipCount -= 1
            temp += 1
        if right - temp + 1 > currMax:
            currMax = right - temp + 1
            left = temp

    for i in range(left, left + currMax):
        result.append(i)

    return result


print(maxContinuousSeriesOf1s([1, 1, 0, 1, 1, 0, 0, 1, 1, 1], 1))  # [0, 1, 2, 3, 4]
print(maxContinuousSeriesOf1s([1, 0, 0, 0, 1, 0, 1], 2))  # [3, 4, 5, 6]
