# Given an array of integers A and an integer B,
# find and return the maximum value K such that there is no subarray in A of size K
# with sum of elements greater than B.
# 1 <= |A| <= 100000
# 1 <= A[i] <= 10^9
# 1 <= B <= 10^9
def binarySearch(prefixSumList, N, B):
    result = -1
    start = 1
    end = N
    temp = 0
    while start <= end:
        mid = start + (end - start) // 2
        for i in range(mid, N + 1):
            temp = i
            if prefixSumList[i] - prefixSumList[i - mid] > B:
                temp -= 1
                break
        temp += 1
        if temp == N + 1:
            start = mid + 1
            result = mid
        else:
            end = mid - 1

    return result


def specialInteger(A, B):
    N = len(A)
    prefixSumList = []
    for i in range(N + 1):
        prefixSumList.append(0)

    for i in range(N):
        prefixSumList[i + 1] = prefixSumList[i] + A[i]

    return binarySearch(prefixSumList, N, B)


print(specialInteger([1, 2, 10, 4], 14))  # 2
print(specialInteger([1, 2, 3, 4, 5], 10))  # 2
print(specialInteger([5, 17, 100, 11], 130))  # 3
