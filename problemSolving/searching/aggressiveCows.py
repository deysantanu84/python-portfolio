# Farmer John has built a new long barn, with N stalls.
# Given an array of integers A of size N where each element of the array
# represents the location of the stall, and an integer B which represent the number of cows.
# His cows don't like this barn layout and become aggressive towards each other once put into a stall.
# To prevent the cows from hurting each other, John wants to assign the cows to the stalls,
# such that the minimum distance between any two of them is as large as possible.
# What is the largest minimum distance?
# 2 <= N <= 100000
# 0 <= A[i] <= 10^9
# 2 <= B <= N
# The first argument given is the integer array A.
# The second argument given is the integer B.
# Return the largest minimum distance possible among the cows.
def aggressiveCows(A, B):
    N = len(A)
    A.sort()
    start = 0
    end = A[-1]
    result = 0
    while start <= end:
        mid = start + (end - start) // 2
        count = 1
        left = 0
        for i in range(1, N):
            if A[i] - A[left] >= mid:
                left = i
                count += 1
                if count == B:
                    break
        if count >= B:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    return result


print(aggressiveCows([1, 2, 3, 4, 5], 3))  # 2
# John can assign the stalls at location 1,3 and 5 to the 3 cows respectively.
# So the minimum distance will be 2.

print(aggressiveCows([5, 17, 100, 11], 2))  # 95
print(aggressiveCows([1, 2], 2))  # 1
# The minimum distance will be 1.
