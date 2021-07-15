# Given a vector A of non-negative integers representing an elevation map
# where the width of each bar is 1, compute how much water it is able to trap after raining.
def rainWaterTrapped(A):
    trappedWater = 0
    i = 0
    j = len(A) - 1
    lMax = 0
    rMax = 0
    while i <= j:
        if A[i] < A[j]:
            if A[i] > lMax:
                lMax = A[i]
            else:
                trappedWater += lMax - A[i]
            i += 1
        else:
            if A[j] > rMax:
                rMax = A[j]
            else:
                trappedWater += rMax - A[j]
            j -= 1
    return trappedWater


print(rainWaterTrapped([0, 1, 0, 2]))  # 1
print(rainWaterTrapped([1, 2]))  # 0
print(rainWaterTrapped([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # 6
