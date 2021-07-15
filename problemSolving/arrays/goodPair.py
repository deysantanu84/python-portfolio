# Given an array A and a integer B.
# A pair(i,j) in the array is a good pair if i!=j and (A[i]+A[j]==B).
# Check if any good pair exist or not. Return 1 if good pair exist otherwise return 0.
def solve(A, B):
    for i in range(len(A)-1):
        for j in range(i, len(A)):
            if i != j and A[i] + A[j] == B:
                return 1
    return 0


print(solve([1, 2, 3, 4], 7))
print(solve([1, 2, 4], 4))
print(solve([1, 2, 2], 4))
