# Given two binary strings, return their sum (also a binary string).
def addBinary2(A, B):
    maxStrLen = max(len(A), len(B))
    A = A.zfill(maxStrLen)
    B = B.zfill(maxStrLen)
    result = ''
    carry = 0

    for index in range(maxStrLen - 1, -1, -1):
        tempCarry = carry
        if A[index] == '1':
            tempCarry += 1
        else:
            tempCarry += 0

        if B[index] == '1':
            tempCarry += 1
        else:
            tempCarry += 0

        if tempCarry % 2:
            result += '1'
        else:
            result += '0'

        if tempCarry < 2:
            carry = 0
        else:
            carry = 1

    if carry:
        result = '1' + result

    return result.zfill(maxStrLen)


def addBinary(A, B):
    maxStrLen = max(len(A), len(B))
    A = A.zfill(maxStrLen)
    B = B.zfill(maxStrLen)
    result = ''
    carry = 0

    for index in range(maxStrLen - 1, -1, -1):
        tempCarry = carry
        tempCarry += 1 if A[index] == '1' else 0
        tempCarry += 1 if B[index] == '1' else 0
        result = ('1' if tempCarry % 2 == 1 else '0') + result
        carry = 0 if tempCarry < 2 else 1

    if carry != 0:
        result = '1' + result

    return result.zfill(maxStrLen)


# print(addBinary2('100', '11'))
# print(addBinary2('1010110111001101101000', '1000011011000000111100110')) -- wrong answer
print(addBinary('1010110111001101101000', '1000011011000000111100110'))
