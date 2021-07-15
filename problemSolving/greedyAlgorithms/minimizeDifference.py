# Given an array of integers A of size, N. Minimize the absolute difference between the maximum and
# minimum element of the array.
# You can perform two types of operations at most B times in total to change the values in the array.
# Multiple operations can be performed on the same element.
# Increment : A[i] -> A[i] + 1.
# Decrement : A[i] -> A[i] - 1.
# Return the minimum difference possible.
# 1 <= N <= 10^5
# 1 <= A[i] <= 10^6
# 1 <= B <= 10^9
# First argument is an integer array A.
# Second argument is an integer B which represents the maximum number of operations that can be performed.
# Return an integer denoting the minimum difference.
import sys
INT_MIN = -sys.maxsize
INT_MAX = sys.maxsize - 1


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        N = len(A)
        freqList = [0 for _ in range(10**6 + 10)]
        tempMin = INT_MAX
        tempMax = INT_MIN

        for i in range(N):
            freqList[A[i]] += 1
            if A[i] < tempMin:
                tempMin = A[i]
            if A[i] > tempMax:
                tempMax = A[i]

        result = tempMax - tempMin
        freqMin = freqList[tempMin]
        freqMax = freqList[tempMax]

        while tempMin < tempMax:
            if B < min(freqMin, freqMax):
                break

            if freqMin < freqMax:
                B -= freqMin
                freqMin += freqList[tempMin + 1]
                tempMin += 1
            else:
                B -= freqMax
                freqMax += freqList[tempMax - 1]
                tempMax -= 1

            result = tempMax - tempMin

        return result


sol = Solution()
print(sol.solve([2, 6, 3, 9, 8], 3))  # 5
print(sol.solve([4, 6, 3, 1, 4], 5))  # 1
