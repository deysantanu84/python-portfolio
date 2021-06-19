# You are given 2 numbers P and Q.
# An operation on these 2 numbers is defined as follows: Take the smaller number of the 2 numbers
# and subtract it from the bigger number. Keep performing this operation till either of the
# following criterion is met:
# Both numbers become equal.
# Either of the number becomes 0.
# Find the sum of the final values of P and Q.
# 0 <= P,Q <= 1e9
# TLE
def repeatedSubtraction(A, B):
    while A != B and A != 0 and B != 0:
        if A > B:
            A -= B
        else:
            B -= A

    return A + B


print(repeatedSubtraction(5, 15))  # 10
