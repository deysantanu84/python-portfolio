# https://www.hackerrank.com/challenges/a-very-big-sum/problem
# Complete the aVeryBigSum function below.
def aVeryBigSum(arr):
    digitSumList = [0] * 10

    for index in range(ar_count):
        currInteger = str(arr[index])
        for index1 in range(len(currInteger)):
            digitSumList[index1] += int(currInteger[index1])

    for index2 in range(len(digitSumList)-1, 0, -1):
        if digitSumList[index2] > 9:
            carry = digitSumList[index2] / 10
            digitSumList[index2] %= 10
            digitSumList[index2 - 1] += int(carry)

    return int("".join(map(str, digitSumList)))


if __name__ == '__main__':
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = aVeryBigSum(ar)
    print(result)
