# Given an array of positive integers A, check and return
# whether the array elements are consecutive or not.
# NOTE: Try this with O(1) extra space.
# 1 <= length of the array <= 100000
# 1 <= A[i] <= 10^9
# Return 1 if the array elements are consecutive else return 0.
def consecutiveElements(A):
    A.sort()
    for i in range(len(A) - 1):
        if A[i + 1] - A[i] != 1:
            return 0

    return 1


print(consecutiveElements([3, 2, 1, 4, 5]))  # 1
print(consecutiveElements([1, 3, 2, 5]))  # 0
