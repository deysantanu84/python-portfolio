# Given an array of integers A, find and return
# whether the given array contains a non-empty sub-array with a sum equal to 0.
# If the given array contains a sub-array with sum zero return 1 else return 0.
# TLE with Dict
def subArray0Sum(A):
    tempSum = 0
    sumSet = set()

    for i in range(len(A)):
        tempSum += A[i]
        if tempSum == 0 or tempSum in sumSet:
            return 1
        sumSet.add(tempSum)
    return 0


print(subArray0Sum([1, 2, 3, 4, 5]))  # 0
print(subArray0Sum([-1, 1]))  # 1
print(subArray0Sum([5, 17, -22, 11]))  # 1
print(subArray0Sum([96, -71, 18, 66, -39, -32, -16, -83, -11, -92, 55, 66, 93, 5, 50, -45, 66, -28, 69, -4, -34, -87, -32, 7, -53, 33, -12, -94, -80, -71, 48, -93, 62]))  # 1
print(subArray0Sum([-46, -16, 74, 18, 33, 20, -2, -7, 90, 100, -60, 12, -39, -3, 14, 95, -65, -38, 38, 75, -35, 32, -67, 58, 78, -91, 54, 52, 67, -43, -51, -75, -67, 4, 25, -22, 53, -33]))  # 1
