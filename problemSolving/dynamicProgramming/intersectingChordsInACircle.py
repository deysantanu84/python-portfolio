# Given a number A, return number of ways you can draw A chords in a circle with 2 x A points
# such that no 2 chords intersect.
# Two ways are different if there exists a chord which is present in one way and not in other.
# Return the answer modulo 10^9 + 7.
# 1 <= A <= 10^3
# The first and the only argument contains the integer A.
# Return an integer answering the query as described in the problem statement.
import sys
sys.setrecursionlimit(10**9)


class Solution:
    def util(self, A, resultList):
        if not A:
            return 1

        if resultList[A] is None:
            result = 0

            for i in range(A):
                result += self.util(i, resultList) * self.util(A - 1 - i, resultList)

            resultList[A] = result % (10**9 + 7)

        return resultList[A]

    # @param A : integer
    # @return an integer
    def chordCnt(self, A):
        resultList = [None] * (A + 1)
        return self.util(A, resultList)


sol = Solution()
print(sol.chordCnt(1))  # 1
print(sol.chordCnt(2))  # 2
