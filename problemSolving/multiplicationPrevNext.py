# Given an array of integers A,
# update every element with multiplication of previous and next elements with following exceptions.
# a) First element is replaced by multiplication of first and second.
# b) Last element is replaced by multiplication of last and second last.
def solve(A):
    if len(A) <= 1:
        return A
    result = A.copy()
    result[0] = A[0] * A[1]
    result[-1] = A[-1] * A[-2]
    for i in range(1, len(A)-1):
        result[i] = A[i-1] * A[i+1]

    return result


print(solve([]))
print(solve([0]))
print(solve([0, 1]))
print(solve([1, 2, 3, 4, 5]))
print(solve([5, 17, 100, 11]))
