# Scooby has 3 three integers A, B and C.
# Scooby calls a positive integer special if it is divisible by B and it is divisible by C.
# You need to tell number of special integers less than or equal to A.
# 1 <= A, B, C <= 10^9
# A = 12, B = 3, C = 2  # 2
# A = 6, B = 1, C = 4  # 1
from math import gcd


def divisorGame(A, B, C):
    count = 0
    divisor = abs(B * C) // gcd(B, C)
    for i in range(divisor, A + 1, divisor):
        count += 1
    return count


print(divisorGame(12, 3, 2))  # 2
print(divisorGame(6, 1, 4))  # 1
print(divisorGame(1000000000, 10000, 10000))  # 100000
print(divisorGame(1000000000, 1000000000, 1000000000))  # 1
