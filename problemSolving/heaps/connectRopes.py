# Given an array of integers A representing the length of ropes.
# You need to connect these ropes into one rope.
# The cost of connecting two ropes is equal to the sum of their lengths.
# Find and return the minimum cost to connect these ropes into one rope.
# 1 <= length of the array <= 100000
# 1 <= A[i] <= 1000
# The only argument given is the integer array A.
# Return an integer denoting the minimum cost to connect these ropes into one rope.
from heapq import heapify, heappop, heappush


def solve(A):
    result = 0
    heapify(A)

    while len(A) > 1:
        first = heappop(A)
        second = heappop(A)

        result += first + second
        heappush(A, first + second)

    return result


print(solve([1, 2, 3, 4, 5]))  # 33
print(solve([5, 17, 100, 11]))  # 182
