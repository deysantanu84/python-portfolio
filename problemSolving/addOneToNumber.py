# Given a non-negative number represented as an array of digits,
# add 1 to the number ( increment the number represented by the digits ).
# The digits are stored such that the most significant digit is at the head of the list.
# NOTE: Certain things are intentionally left unclear in this question which you should
# practice asking the interviewer. For example: for this problem, following are some good questions to ask :
# Q : Can the input have 0's before the most significant digit. Or in other words, is 0 1 2 3 a valid input?
# A : For the purpose of this question, YES
# Q : Can the output have 0's before the most significant digit? Or in other words, is 0 1 2 4 a valid output?
# A : For the purpose of this question, NO. Even if the input has zeroes before the most significant digit.
def addOneToNumber(A):
    number = 0
    result = []
    N = len(A)
    # for i in range(N):
    #     number += A[i] * (10 ** (N-i-1))
    number = int("".join(map(str, A)))
    number += 1
    # M = len(str(number))
    # for i in range(M):
    #     result.append(0)
    # for i in range(M):
    #     rem = number % 10
    #     result[M-i-1] = rem
    #     number //= 10
    result = [int(x) for x in str(number)]
    return result


print(addOneToNumber([1, 2, 3]))
print(addOneToNumber([0, 1, 2, 3]))
