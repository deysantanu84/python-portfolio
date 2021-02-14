# https://www.hackerrank.com/challenges/python-time-delta/problem

from datetime import datetime

dateFormat = '%a %d %b %Y %H:%M:%S %z'
n = int(input())  # number of test cases
for i in range(n):
    t1 = datetime.strptime(input(), dateFormat)
    t2 = datetime.strptime(input(), dateFormat)

    print(int(abs((t1-t2).total_seconds())))
