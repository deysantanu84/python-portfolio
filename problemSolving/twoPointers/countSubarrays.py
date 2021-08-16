# Misha likes finding all sub-arrays of an Array.
# Now she gives you an array A of N elements and told you to
# find the number of sub-arrays of A, that have unique elements.
# Since the number of sub-arrays could be large, return value % 10^9 +7.
# 1 <= N <= 10^5
# 1 <= A[i] <= 10^6
# Return the number of sub-arrays of A, that have unique elements.
def countSubarrays(A):
    start = 0
    end = 1
    result = 1
    tempDict = {A[0]: 0}

    while end < len(A):
        if A[end] in tempDict.keys():
            if tempDict[A[end]] >= start:
                start = tempDict[A[end]] + 1
            tempDict[A[end]] = end
        else:
            tempDict[A[end]] = end

        result += end - start + 1
        end += 1

    return result % (10**9 + 7)


print(countSubarrays([1, 1, 3]))  # 4
# Subarrays of A that have unique elements only: [1], [1], [1, 3], [3]

print(countSubarrays([2, 1, 2]))  # 5
# Subarrays of A that have unique elements only: [2], [1], [2, 1], [1, 2], [2]

print(countSubarrays([5, 2, 3, 5, 4, 3]))  # 16
print(countSubarrays([93, 9, 12, 32, 97, 75, 32, 77, 40, 79, 61, 42, 57, 19, 64, 16, 86, 47, 41, 67, 76, 63, 24, 10,
                      25, 96, 1, 30, 73, 91, 70, 65, 53, 75, 5, 19, 65, 6, 96, 33, 73, 55, 4, 90, 72, 83, 54, 78, 67,
                      56, 8, 70, 43, 63]))
# 775

print(countSubarrays([54, 5, 31, 87, 45, 35, 59, 71, 18, 66, 79, 39, 46, 24, 91, 95, 63, 51, 34, 47, 33, 48, 56, 27,
                      23, 4, 3, 74, 81, 57, 23, 71, 83, 53, 90, 31, 34, 75, 15, 81, 10, 71, 82, 71, 3, 100, 43, 100,
                      67, 16, 59, 45, 73, 57, 76, 40, 45, 38, 37, 20, 24, 72, 10, 53, 29, 77, 99, 98, 59, 85, 89, 20,
                      53, 73]))
# 878
