# Given three integers A, B and C, where A represents n, B represents r and C represents p
# and p is a prime number greater than equal to n, find and return the value of
# nCr % p where nCr % p = (n! / ((n-r)! * r!)) % p.
# x! means factorial of x i.e. x! = 1 * 2 * 3... * x.
# NOTE: For this problem, we are considering 1 as a prime.
# 1 <= A <= 10^6
# 1 <= B <= A
# A <= C <= 10^9+7
# The first argument given is the integer A ( = n).
# The second argument given is the integer B ( = r).
# The third argument given is the integer C ( = p).
# Return the value of nCr % p.
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        numerator = 1
        denominator = 1

        if A == B:
            return 1 % C

        for i in range(min(B, (A - B))):
            numerator = (numerator * (A - i)) % C
            denominator = (denominator * (i + 1)) % C

        return (numerator * pow(denominator, C-2, C)) % C


sol = Solution()
print(sol.solve(5, 2, 13))  # 10
print(sol.solve(6, 2, 13))  # 2
print(sol.solve(8, 3, 191))  # 56
print(sol.solve(1, 1, 1))  # 0
print(sol.solve(37924, 18904, 624097))  # 570378
print(sol.solve(43150, 21762, 941489))  # 16006
