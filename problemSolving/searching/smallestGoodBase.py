# Given an integer A, we call k >= 2 a good base of A, if all digits of A base k are 1.
# Now given a string representing A, you should return the smallest good base of A in string format.
def binarySearch(A, N):
    start = 1
    end = A
    while start <= end:
        mid = start + (end - start) // 2
        tempSum = 0
        temp = 1
        for i in range(N):
            tempSum += temp
            temp *= mid
        if tempSum == A:
            return mid
        elif tempSum > A:
            end = mid - 1
        else:
            start = mid + 1
    return -1


def smallestGoodBase(A):
    A = int(A)
    for i in range(64, 0, -1):
        result = binarySearch(A, i)
        if result >= 2:
            return str(result)
    return str(A - 1)


print(smallestGoodBase("121"))  # "3"
print(smallestGoodBase("13"))  # "3"
print(smallestGoodBase("4681"))  # "8"
