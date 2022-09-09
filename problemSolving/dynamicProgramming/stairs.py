# You are climbing a stair case and it takes A steps to reach to the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# 1 <= A <= 36
# The first and the only argument contains an integer A, the number of steps.
# Return an integer, representing the number of ways to reach the top.

# Recurrence relation is same as fibonacci series
# Bottom-up (Iterative) solution
class Solution:
    # @param A : integer
    # @return an integer
    def climbStairs(self, A):
        if A == 1:
            return 1

        resultList = [0] * (A + 1)
        resultList[1] = 1
        resultList[2] = 2

        for i in range(3, A + 1):
            resultList[i] = resultList[i-1] + resultList[i-2]

        return resultList[-1]


sol = Solution()
print(sol.climbStairs(2))  # 2
print(sol.climbStairs(3))  # 3
print(sol.climbStairs(36))  # 24157817
