# Given three integers A, B and C, where A represents n, B represents r and C represents m,
# find and return the value of nCr % m where nCr % m = (n!/((n-r)!*r!))% m.
# x! means factorial of x i.e. x! = 1 * 2 * 3... * x.
# 1 <= A * B <= 10^6
# 1 <= B <= A
# 1 <= C <= 10^6
# The first argument given is integer A ( = n).
# The second argument given is integer B ( = r).
# The third argument given is integer C ( = m).
# Return the value of nCr % m.
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        result = [0 for _ in range(B + 1)]
        result[0] = 1

        for i in range(1, A + 1):
            for j in range(min(i, B), 0, -1):
                result[j] = (result[j] + result[j - 1]) % C

        return result[-1]


sol = Solution()
print(sol.solve(5, 2, 13))  # 10
print(sol.solve(6, 2, 13))  # 2
