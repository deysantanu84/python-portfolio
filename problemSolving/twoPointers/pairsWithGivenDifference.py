# Given an one-dimensional integer array A of size N and an integer B.
# Count all distinct pairs with difference equal to B.
# Here a pair is defined as an integer pair (x, y),
# where x and y are both numbers in the array and their absolute difference is B.
# 1 <= N <= 10^4
# 0 <= A[i], B <= 10^5
def pairsWithGivenDifference(A, B):
    result = 0
    N = len(A)
    A.sort()
    left = 0
    right = 1
    resultPairDict = {}

    while right < N:
        if A[right] - A[left] == B:
            if A[left] not in resultPairDict.keys():
                resultPairDict[A[left]] = A[right]
                result += 1
            else:
                if A[right] != resultPairDict[A[left]]:
                    result += 1
            left += 1
            right += 1

        elif A[right] - A[left] > B:
            left += 1
            if left == right:
                right += 1
        else:
            right += 1
    return result


print(pairsWithGivenDifference([1, 5, 3, 4, 2], 3))  # 2
print(pairsWithGivenDifference([8, 12, 16, 4, 0, 20], 4))  # 5
print(pairsWithGivenDifference([1, 1, 1, 2, 2], 0))  # 2
print(pairsWithGivenDifference([1, 2], 0))  # 0
