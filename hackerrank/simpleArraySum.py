# https://www.hackerrank.com/challenges/simple-array-sum/problem

import os
# import sys


# Complete the simpleArraySum function below.
def simpleArraySum(arr):
    arraySum = 0
    for i in arr:
        arraySum += i
    return arraySum


if __name__ == '__main__':
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = simpleArraySum(ar)
    print(result)
