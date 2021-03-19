# Given a array A of non negative integers, arrange them such that they form the largest number.
# Note: The result may be very large, so you need to return a string instead of an integer.
# https://www.geeksforgeeks.org/given-an-array-of-numbers-arrange-the-numbers-to-form-the-biggest-number/#:~:text=Given%20an%20array%20of%20numbers,998764543431%20gives%20the%20largest%20value.
# https://www.geeksforgeeks.org/arrange-given-numbers-form-biggest-number-set-2/
from itertools import permutations


def largestInteger2(A):
    result = []
    for item in permutations(A, len(A)):
        result.append("".join(map(str, item)))
    return max(result)


def largestInteger(A):
    result = []
    resultStr = ""
    length = len(str(max(A))) + 1

    for item in A:
        temp = str(item) * length
        result.append((temp[:length], item))
    result.sort(reverse=True)

    for item in result:
        resultStr += str(item[1])

    if int(resultStr) == 0:
        return "0"

    return resultStr


print(largestInteger([3, 30, 34, 5, 9]))  # "9534330"
print(largestInteger([2, 3, 9, 0]))  # "9320"
