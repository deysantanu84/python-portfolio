# Given an integer A representing the number of square blocks.
# The height of each square block is 1.
# The task is to create a staircase of max height using these blocks.
# The first stair would require only one block, the second stair would require two blocks and so on.
# Find and return the maximum height of the staircase.
# 0 <= A <= 10^9
def maxStaircaseHeight(A):
    if A == 0:
        return A

    start = 1
    end = A
    result = 1
    while start <= end:
        mid = start + (end - start) // 2
        if (mid * (mid + 1)) / 2 <= A:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    return result


print(maxStaircaseHeight(10))  # 4
print(maxStaircaseHeight(20))  # 5
