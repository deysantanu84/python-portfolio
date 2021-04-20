# Given three positive integers A, B and C.
# Any positive integer is magical if it is divisible by either B or C.
# Return the Ath magical number. Since the answer may be very large, return it modulo 10^9 + 7.
# 1 <= A <= 10^9
# 2 <= B, C <= 40000
from math import gcd


def AthMagicalNumber(A, B, C):
    lcm = B * C // gcd(B, C)
    start = 2
    end = 10 ** 14
    while start <= end:
        mid = start + (end - start) // 2
        n = mid // B + mid // C - mid // lcm
        if n >= A:
            end = mid - 1
        else:
            start = mid + 1
    return start % (10 ** 9 + 7)


print(AthMagicalNumber(1, 2, 3))  # 2
print(AthMagicalNumber(4, 2, 3))  # 6
