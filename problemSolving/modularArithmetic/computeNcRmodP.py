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
# TLE
class Solution:
    def factPower(self, n, p):
        k = 0

        while n > 0:
            k += n // p
            n //= p

        return k

    def powerMod(self, a, b, mod):
        x = 1
        y = a

        while b > 0:
            if b % 2 == 1:
                x = (x*y)
                if x > mod:
                    x %= mod

            y = (y*y)
            if y > mod:
                y %= mod
            b //= 2

        return x

    def util(self, n, r, mod):
        result = 1
        primeList = [True for _ in range(n + 1)]

        for i in range(2, n + 1):
            if primeList[i]:
                for j in range(2 * i, n + 1, i):
                    primeList[j] = False

                k = self.factPower(n, i) - self.factPower(r, i) - self.factPower(n - r, i)
                result = (result * self.powerMod(i, k, mod)) % mod

        return result

    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        if C == 1:
            return 0

        else:
            return self.util(A, B, C)


sol = Solution()
print(sol.solve(5, 2, 13))  # 10
print(sol.solve(6, 2, 13))  # 2
print(sol.solve(8, 3, 191))  # 56
