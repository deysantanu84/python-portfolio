# Given an array A of length N. You have to answer Q queries.
# Each query will contain 4 integers l1, r1, l2 and r2.
# If sorted segment from [l1, r1] is same as sorted segment from [l2 r2] then answer is 1 else 0.
# NOTE The queries are 0-indexed.
# 0 <= A[i] <= 100000
# 1 <= N <= 100000
# 1 <= Q <= 100000
# First argument is an array A.
# Second will be 2-D array B denoting queries with dimension Q * 4.
# Consider ith query as l1 = B[i][0], r1 = B[i][1], l2 = A[i][2], r2 = B[i][3].
# Return an array of length Q with answer of the queries in the same order in input.
from random import randint
tempDict = {}


class Solution:
    def randUtil(self):
        ret = 0
        ret |= randint(0, 1 << 20)
        x = randint(0, 1 << 20)
        ret |= (x << 15)

        return ret

    def setHash(self, A):
        N = len(A)
        for i in range(N):
            if not tempDict.get(A[i]):
                tempDict[A[i]] = self.randUtil()

    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        N = len(A)
        self.setHash(A)
        temp = [0] * N
        temp[0] = tempDict[A[0]]

        for i in range(1, N):
            temp[i] = temp[i-1] + tempDict[A[i]]

        M = len(B)
        result = [0] * M
        for i in range(M):
            l1, r1 = B[i][0], B[i][1]
            l2, r2 = B[i][2], B[i][3]

            if l1 > 0:
                sum1 = temp[r1] - temp[l1-1]
            else:
                sum1 = temp[r1]

            if l2 > 0:
                sum2 = temp[r2] - temp[l2 - 1]
            else:
                sum2 = temp[r2]

            if sum1 == sum2:
                result[i] = 1
            else:
                result[i] = 0

        return result


sol = Solution()
print(sol.solve([1, 7, 11, 8, 11, 7, 1], [[0, 2, 4, 6]]))  # [1]
print(sol.solve([1, 3, 2], [[0, 1, 1, 2]]))  # [0]
print(sol.solve([100000, 100000, 100000, 100000, 100000],
                [[0, 3, 1, 4], [0, 1, 2, 3], [4, 4, 1, 1], [1, 3, 0, 0], [2, 4, 1, 1]]))  # [1, 1, 1, 0, 0]
