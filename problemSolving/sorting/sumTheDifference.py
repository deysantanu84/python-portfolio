# Given an integer array A of size N.
# You have to find all possible non-empty subsequence of the array of numbers
# and then, for each subsequence, find the difference between the largest and smallest numbers
# in that subsequence Then add up all the differences to get the number.
# As the number may be large, output the number modulo 1e9 + 7 (1000000007).
# NOTE: Subsequence can be non-contiguous.
# 1 <= N <= 10000
# 1<= A[i] <=1000
def sumTheDifference(A):
    result = 0
    N = len(A)
    A.sort()
    for i in range(1, N + 1):
        result += (A[i - 1] * (2**(i - 1) - 2**(N - i))) % (10**9 + 7)

    return result % (10**9 + 7)


print(sumTheDifference([1, 2]))  # 1
print(sumTheDifference([1]))  # 0
print(sumTheDifference([1, 2, 3]))  # 6
