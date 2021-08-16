# Given an array of integers A .
# value of a array = max(array) - min(array).
# Calculate and return the sum of values of all possible subarrays of A % 10^9+7.
# 1 <= |A| <= 100000
# 1 <= A[i] <= 1000000
# The first and only argument given is the integer array A.
# Return the sum of values of all possible subarrays of A % 10^9+7.
# TLE
class Solution:
    def leftSmallerNearest(self, A):
        N = len(A)
        result = [0 for _ in range(N)]
        stack = []

        for i in range(N):
            while len(stack) and A[i] <= A[stack[-1]]:
                stack.pop()

            if not len(stack):
                result[i] = -1

            elif A[i] > A[stack[-1]]:
                result[i] = stack[-1]

            stack.append(i)

        return result

    def rightSmallerNearest(self, A):
        N = len(A)
        result = [0 for _ in range(N)]
        stack = []

        for i in range(N - 1, -1, -1):
            while len(stack) and A[i] < A[stack[-1]]:
                stack.pop()

            if not len(stack):
                result[i] = N

            elif A[i] >= A[stack[-1]]:
                result[i] = stack[-1]

            stack.append(i)

        return result

    def leftLargerNearest(self, A):
        N = len(A)
        result = [0 for _ in range(N)]
        stack = []

        for i in range(N):
            while len(stack) and A[i] >= A[stack[-1]]:
                stack.pop()

            if not len(stack):
                result[i] = -1

            elif A[i] < A[stack[-1]]:
                result[i] = stack[-1]

            stack.append(i)

        return result

    def rightLargerNearest(self, A):
        N = len(A)
        result = [0 for _ in range(N)]
        stack = []

        for i in range(N - 1, -1, -1):
            while len(stack) and A[i] > A[stack[-1]]:
                stack.pop()

            if not len(stack):
                result[i] = N

            elif A[i] <= A[stack[-1]]:
                result[i] = stack[-1]

            stack.append(i)

        return result

    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        result = 0
        N = len(A)
        leftSmallList = self.leftSmallerNearest(A)
        rightSmallList = self.rightSmallerNearest(A)
        leftLargeList = self.leftLargerNearest(A)
        rightLargeList = self.rightLargerNearest(A)

        for i in range(N):
            left1 = leftSmallList[i]
            right1 = rightSmallList[i]
            left2 = leftLargeList[i]
            right2 = rightLargeList[i]

            tempMin = (i - left1) * (right1 - i)
            tempMax = (i - left2) * (right2 - i)
            result += A[i] * (tempMax - tempMin)

        return result % (10**9 + 7)


sol = Solution()
print(sol.solve([1]))  # 0
print(sol.solve([4, 7, 3, 8]))  # 26
