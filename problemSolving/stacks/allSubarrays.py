# Given an integer array A of size N. You have to generate it's all subarrays having the size greater than 1.
# Then for each subarray find Bitwise XOR of its maximum and second maximum element.
# Find and return the maximum value of XOR among all subarrays.
# 2 <= N <= 10^5
# 1 <= A[i] <= 10^7
def allSubarrays(A):
    stack = []
    length = 0
    result1 = 0

    for item in A:
        while stack and stack[-1] < item:
            stack.pop()
            length -= 1

        stack.append(item)
        length += 1

        if length > 1:
            result1 = max(result1, stack[-1] ^ stack[-2])

    result2 = 0

    stack.clear()
    length = 0

    A.reverse()

    for item in A:
        while stack and stack[-1] < item:
            stack.pop()
            length -= 1

        stack.append(item)
        length += 1

        if length > 1:
            result2 = max(result2, stack[-1] ^ stack[-2])

    return max(result1, result2)


print(allSubarrays([2, 3, 1, 4]))  # 7
print(allSubarrays([1, 3]))  # 2
