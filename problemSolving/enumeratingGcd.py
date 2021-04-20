# You are given a number A and a number B.
# Greatest Common Divisor (GCD) of all numbers between A and B inclusive is taken (GCD(A, A+1, A+2 ... B)).
# As this problem looks a bit easy, it is given that numbers A and B can be in the range of 10^100.
# You have to return the value of GCD found.
# Greatest common divisor of 2 numbers A and B is the largest number D that divides both A and B perfectly.
# 1 <= A <= B <= 10^100
# First argument is a string denoting A.
# Second argument is a string denoting B.
# Return a string which contains the digits of the integer which represents the GCD.
# The returned string should not have any leading zeroes.
def euclideanGcd(a, b):
    if b == 0:
        return a
    else:
        return euclideanGcd(b, a % b)


def enumerateGcd(A, B):
    if int(A) == int(B):
        return A

    gcd = euclideanGcd(int(A), int(B))
    for i in range(int(A) + 1, int(B)):
        gcd = euclideanGcd(gcd, i)
    return str(gcd)


print(enumerateGcd('1', '3'))  # '1'
