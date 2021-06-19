# Given an array with n objects colored red, white or blue,
# sort them so that objects of the same color are adjacent,
# with the colors in the order red, white and blue.
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
# Note: Using library sort function is not allowed.
def sortByColor(A):
    low = 0
    mid = 0
    high = len(A) - 1
    while mid <= high:
        if A[mid] == 0:
            A[low], A[mid] = A[mid], A[low]
            low += 1
            mid += 1
        elif A[mid] == 2:
            A[high], A[mid] = A[mid], A[high]
            high -= 1
        else:
            mid += 1
    return A


print(sortByColor([0, 1, 2, 0, 1, 2]))
# print(sortByColor([0]))
