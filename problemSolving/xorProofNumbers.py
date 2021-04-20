def sumOfDigits(x):
    result = 0
    while x:
        result += x % 10
        x = x // 10
    return result


# TLE
def xorProofIntegerCount(A, B):
    count = 0
    for integer in range(10, B + 1):
        if integer ^ sumOfDigits(integer) >= A:
            count += 1
    return count


print(xorProofIntegerCount(2, 11))  # 2
print(xorProofIntegerCount(12, 12))  # 1
