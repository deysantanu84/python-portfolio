def solve(N, A):
    if A[0] > A[1]:
        A[0] = A[1] // 2

    for i in range(1, N - 1):
        if((A[i - 1] < A[i] and A[i + 1] < A[i])
                or (A[i - 1] > A[i] and A[i + 1] > A[i])):
            A[i] = (A[i - 1] + A[i + 1]) // 2
            if A[i] == A[i - 1] or A[i] == A[i + 1]:
                return "No"
    return "Yes"


T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    out_ = solve(N, A)
    print(out_)
