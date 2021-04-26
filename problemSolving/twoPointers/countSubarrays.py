# Misha likes finding all sub-arrays of an Array.
# Now she gives you an array A of N elements and told you to
# find the number of sub-arrays of A, that have unique elements.
# Since the number of sub-arrays could be large, return value % 10^9 +7.
# 1 <= N <= 10^5
# 1 <= A[i] <= 10^6
# Return the number of sub-arrays of A, that have unique elements.
# Python 3 program to calculate sum of
# lengths of subarrays of distinct elements.

# Returns sum of lengths of all subarrays
# with distinct elements.
def countSubarrays(A):
    N = len(A)
    temp = []
    end = 0
    result = []

    for item in A:
        temp.append(item)
        result.append(temp[:])
        temp = []

    for start in range(N):
        while end < N and (A[end] not in temp):
            temp.append(A[end])
            end += 1
        if temp not in result:
            result.append(temp[:])

        temp.remove(A[start])
    return len(result)


print(countSubarrays([1, 1, 3]))  # 4
# Subarrays of A that have unique elements only: [1], [1], [1, 3], [3]

print(countSubarrays([2, 1, 2]))  # 5
# Subarrays of A that have unique elements only: [2], [1], [2, 1], [1, 2], [2]

print(countSubarrays([5, 2, 3, 5, 4, 3]))  # 11
print(countSubarrays([93, 9, 12, 32, 97, 75, 32, 77, 40, 79, 61, 42, 57, 19, 64, 16, 86, 47, 41, 67, 76, 63, 24, 10, 25, 96, 1, 30, 73, 91, 70, 65, 53, 75, 5, 19, 65, 6, 96, 33, 73, 55, 4, 90, 72, 83, 54, 78, 67, 56, 8, 70, 43, 63]))
# 775
