# Given an integer A.
# Compute and return the square root of A.
# If A is not a perfect square, return floor(sqrt(A)).
# DO NOT USE SQRT FUNCTION FROM STANDARD LIBRARY.
# NOTE: Do not use sort function from standard library.
# Users are expected to solve this in O(log(A)) time.
# 0 <= A <= 10^10
# Return floor(sqrt(A))
def squareRootOfInteger(A):
    if A == 0 or A == 1:
        return A
    low = 1
    high = A
    result = 0
    while low <= high:
        mid = low + (high - low) // 2
        if mid * mid == A:
            return mid
        if mid * mid < A:
            low = mid + 1
            result = mid
        else:
            high = mid - 1
    return result


print(squareRootOfInteger(11))  # 3
print(squareRootOfInteger(9))  # 3
