# Given an array A, having N integers, find the maximum even sum using elements of A only once,
# that is, you can't use one element twice
def findMaxEvenSum(A):
    maxEvenSum = sum(A)
    if not maxEvenSum % 2:
        return maxEvenSum
    
    else:
        for item in sorted(A):
            if item % 2:
                maxEvenSum -= item
                return maxEvenSum


print(findMaxEvenSum([2, 3, 4]))
print(findMaxEvenSum([2, 2, 2]))
print(findMaxEvenSum([8, 55, 35, 68, 86, 3, 38, 48, 92, 97, 78, 14, 57, 25, 24, 17, 77, 97, 71, 31, 40, 46, 40, 57, 18, 94, 84, 0, 22, 4, 21, 80, 74, 71, 76, 20, 48, 43, 68, 32, 67, 0, 23, 7, 6, 25, 94, 5, 35, 65, 93, 74, 13, 32, 41, 31, 49]))
