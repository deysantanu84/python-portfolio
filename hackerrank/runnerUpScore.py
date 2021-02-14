# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr = sorted(arr, reverse=True)
    i = 0
    winnerScore = arr[0]
    while arr[i] == winnerScore:
        i += 1
    print(arr[i])
