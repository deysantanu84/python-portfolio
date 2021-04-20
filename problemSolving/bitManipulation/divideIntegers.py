# Divide two integers without using multiplication, division and mod operator.
# Return the floor of the result of the division.
# Also, consider if there can be overflow cases i.e output is greater than INT_MAX, return INT_MAX.
# NOTE: INT_MAX = 2^31 - 1
# -2^31 <= A, B <= 2^31-1
# B != 0
# First argument is an integer A denoting the dividend.
# Second argument is an integer B denoting the divisor.
# Return an integer denoting the floor value of the division.
def divideIntegers(A, B):
    result = 0
    sign = 1 if A ^ B >= 0 else -1
    A = abs(A)
    B = abs(B)
    for power in range(31, -1, -1):
        if (B << power) <= A:
            result += (1 << power)
            A -= (B << power)
    result = -result if sign == -1 else result
    if not (-2**31 <= result <= 2**31-1):
        return 2**31 - 1
    return result


print(divideIntegers(5, 2))  # 2
print(divideIntegers(7, 1))  # 7
