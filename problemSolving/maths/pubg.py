# There are N players each with strength A[i]. when player i attack player j, player j strength
# reduces to max(0, A[j]-A[i]). When a player's strength reaches zero, it loses the game and
# the game continues in the same manner among other players until only 1 survivor remains.
# Can you tell the minimum health last surviving person can have?
# 1 <= N <= 100000
# 1 <= A[i] <= 1000000
# First and only argument of input contains a single integer array A.
# Return a single integer denoting minimum health of last person.
class Solution:
    def gcd(self, P, Q):
        while Q:
            P, Q = Q, P % Q

        return P

    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        N = len(A)
        result = A[0]

        for i in range(1, N):
            result = self.gcd(result, A[i])

        return result


sol = Solution()
print(sol.solve([6, 4]))  # 2
print(sol.solve([2, 3, 4]))  # 1
