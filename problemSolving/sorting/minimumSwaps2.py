# Given an array of integers A of size N that is a permutation of [0, 1, 2, ..., (N-1)].
# It is allowed to swap any two elements (not necessarily consecutive).
# Find the minimum number of swaps required to sort the array in ascending order.
# 1 <= N <= 100000
# 0 <= A[i] < N
def minimumSwaps2(A):
    N = len(A)

    position = [*enumerate(A)]
    position.sort(key=lambda x: x[1])

    visited = {k: False for k in range(N)}

    result = 0

    for i in range(N):
        if visited[i] or position[i][0] == i:
            continue

        count = 0
        j = i

        while not visited[j]:
            visited[j] = True

            j = position[j][0]
            count += 1

        if count > 0:
            result += (count - 1)

    return result


print(minimumSwaps2([1, 5, 4, 3, 2]))  # 2
print(minimumSwaps2([1, 2, 3, 4, 0]))  # 4
print(minimumSwaps2([2, 0, 1, 3]))  # 2
