# For Given Number A find if its COLORFUL number or not.
# If number A is a COLORFUL number return 1 else return 0.
# What is a COLORFUL Number:
# A number can be broken into different contiguous sub-subsequence parts.
# Suppose, a number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245.
# And this number is a COLORFUL number, since product of every digit of a contiguous subsequence is different.
def colorfulNumber(A):
    numberStr = str(A)
    productsSet = set()

    for i in range(len(numberStr)):
        product = 1
        for j in range(i, len(numberStr)):
            product *= int(numberStr[j].replace('0', '1'))
            if product in productsSet:
                return 0
            else:
                productsSet.add(product)
    return 1


# print(colorfulNumber(23))
# print(colorfulNumber(236))
print(colorfulNumber(206))
