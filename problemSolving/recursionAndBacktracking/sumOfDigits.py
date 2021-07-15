# Given a number A, we need to find sum of its digits using recursion.
def sumOfDigits(A):
    if A == 0:
        return 0
    return A % 10 + sumOfDigits(A // 10)


print(sumOfDigits(46))
print(sumOfDigits(11))
