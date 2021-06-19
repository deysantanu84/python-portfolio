# Given an integer array, find if an integer p exists in the array
# such that the number of integers greater than p in the array equals to p.
# If such an integer is found return 1 else return -1.
def nobleInteger(A):
    A = sorted(A)
    N = len(A)
    for i in range(N - 1):
        if A[i] == A[i+1]:
            continue
        if A[i] == N - i - 1:
            return 1
    if A[N - 1] == 0:
        return 1
    return -1


print(nobleInteger([1, 0, 2, 3, 2]))
print(nobleInteger([1, 0, 2, 3, 3]))
