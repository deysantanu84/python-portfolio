# In Danceland, one person can party either alone or can pair up with another person.
# Can you find in how many ways they can party if there are A people in Danceland?
# Note: Return your answer modulo 10003, as the answer can be large.
# 1 <= A <= 10^5
# Given only argument A of type Integer, number of people in Danceland.
# Return an integer denoting the number of ways people of Danceland can party.

# Recurrence relation: f(i) = f(i - 1) + (i - 1) * f(i - 2)
# Bottom-up (Iterative) solution
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        mod = 10003
        resultList = [0 for _ in range(A + 1)]

        for i in range(A + 1):
            if i <= 2:
                resultList[i] = i % mod
            else:
                resultList[i] = (resultList[i - 1] + (i - 1) * resultList[i - 2]) % mod

        return resultList[A] % mod


sol = Solution()
print(sol.solve(3))  # 4
print(sol.solve(5))  # 26
print(sol.solve(17))  # 5793
