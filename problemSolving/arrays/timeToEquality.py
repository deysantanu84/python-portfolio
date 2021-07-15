# Given an integer array A of size N. In one second you can increase the value of one element by 1.
# Find the minimum time in seconds to make all elements of the array equal.
def solve(A):
    seconds = 0
    maxEntry = max(A)
    for item in A:
        seconds += maxEntry - item

    return seconds


print(solve([2, 4, 1, 3, 2]))
