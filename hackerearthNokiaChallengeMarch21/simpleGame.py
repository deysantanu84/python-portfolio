count = 0


def chooseTile(arr, i, j, Sum, P1Score, P2Score):
    global count
    if j == i + 1:
        if count % 2 == 0:
            P2Score += max(arr[i], arr[j])
        else:
            P1Score += max(arr[i], arr[j])
        count += 1
        print(count, i, j, P1Score, P2Score)
        return P1Score - P2Score
    if count % 2 == 0:
        P2Score = max((Sum - chooseTile(arr, i + 1, j, Sum - arr[i], P1Score + arr[i], P2Score)),
                      (Sum - chooseTile(arr, i, j - 1, Sum - arr[j], P1Score + arr[j], P2Score)))
    else:
        P1Score = max((Sum - chooseTile(arr, i + 1, j, Sum - arr[i], P1Score, P2Score + arr[i])),
                      (Sum - chooseTile(arr, i, j - 1, Sum - arr[j], P1Score, P2Score + arr[j])))
    count += 1
    print(count, i, j, P1Score, P2Score)
    return P1Score - P2Score


def simpleGame(N, Tiles):
    Sum = sum(Tiles)
    return chooseTile(Tiles, 0, N - 1, Sum, 0, 0)


A = []
n = int(input())
for _ in range(n):
    p = int(input())
    A.append(p)
out_ = simpleGame(n, A)
print(out_)

# [8, 15, 3, 7]
# [2, 2, 2, 2]
# [20, 30, 2, 2, 2, 10]
# [-1, 100, 4, -5]  # 92
# [3, 1, 100, 5]  # 97
