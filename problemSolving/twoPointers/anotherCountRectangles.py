# Given a sorted array of distinct integers A and an integer B,
# find and return how many rectangles with distinct configurations
# can be created using elements of this array as length and breadth whose area is lesser than B.
# (Note that a rectangle of 2 x 3 is different from 3 x 2 if we take configuration into view)
# 1 <= |A| <= 100000
# 1 <= A[i] <= 10^9
# 1 <= B <= 10^9
# Return the number of rectangles with distinct configurations with area less than B modulo (10^9 + 7).
def anotherCountRectangles(A, B):
    result = 0
    left = 0
    right = len(A) - 1

    while left <= right:
        if A[left] * A[right] >= B:
            right -= 1
        else:
            result += (2 * (right - left) + 1) % (10**9 + 7)
            left += 1
    return result % (10**9 + 7)


print(anotherCountRectangles([1, 2], 5))  # 4
print(anotherCountRectangles([1, 2], 1))  # 0
