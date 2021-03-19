# Given an integer array A of size N. Return 1 if the array can be
# rearranged to form an arithmetic progression, otherwise, return 0.
# A sequence of numbers is called an arithmetic progression if the difference
# between any two consecutive elements is the same.
import sys
INT_MAX = sys.maxsize - 1


def arithmeticProgression(A):
    apSet = set()
    smallest = INT_MAX
    second_smallest = INT_MAX
    if len(A) == 0:
        return 0
    elif len(A) == 1 or len(A) == 2:
        return 1
    for item in A:
        if item < smallest:
            second_smallest = smallest
            smallest = item
        elif item < second_smallest and item != smallest:
            second_smallest = item
        if item in apSet:
            return 0
        apSet.add(item)
    common_difference = second_smallest - smallest
    for i in range(1, len(A) - 1):
        if second_smallest + common_difference * i not in apSet:
            return 0
    return 1


print(arithmeticProgression([3, 5, 1]))
print(arithmeticProgression([2, 4, 1]))
