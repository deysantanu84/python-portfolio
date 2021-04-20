# Given 2 non negative integers A and B, find gcd(A, B)
# GCD of 2 integers A and B is defined as the greatest integer g
# such that g is a divisor of both A and B. Both A and B fit in a 32 bit signed integer.
# Note: DO NOT USE LIBRARY FUNCTIONS.
def euclidean_gcd(x, y):
    while y:
        x, y = y, x % y
    return x


# Loop
def gcd_1(x, y):
    gcd = 1
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if (x % i == 0) and (y % i == 0):
            gcd = i
    return gcd


# Recursion
def gcd_2(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a == b:
        return a
    if a > b:
        return gcd_2(a - b, b)
    return gcd_2(a, b - a)


# Recursion
def hcf(a, b):
    if b == 0:
        return a
    else:
        return hcf(b, a % b)
