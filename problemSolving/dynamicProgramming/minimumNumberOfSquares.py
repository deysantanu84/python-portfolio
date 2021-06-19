# Given an integer A. Return minimum count of numbers, sum of whose squares is equal to A.
# 1 <= A <= 10^5
# First and only argument is an integer A.
# Return an integer denoting the minimum count.
from math import ceil, sqrt


class Solution:
    # @param A : integer
    # @return an integer
    def countMinSquares(self, A):
        countList = [0, 1, 2, 3]

        for i in range(4, A + 1):
            countList.append(i)

            for x in range(1, int(ceil(sqrt(i))) + 1):
                temp = x ** 2
                if temp > i:
                    break
                else:
                    countList[i] = min(countList[i], 1 + countList[i-temp])

        return countList[A]


sol = Solution()
print(sol.countMinSquares(6))  # 3
print(sol.countMinSquares(5))  # 2
