# https://www.hackerrank.com/challenges/designer-door-mat/problem

from math import ceil

if __name__ == '__main__':
    width, length = map(int, input().split())
    if width <= 0 \
            or width % 2 == 0 \
            or length != 3*width \
            or (width <= 5 or width >= 101) \
            or (length <= 15 or length >= 303):
        print('Invalid input. Try again!!!')

    else:
        a = 'WELCOME'
        b = '-'
        c = '.|.'
        midRow = ceil(width/2) - 1
        for i in range(width):
            if i < midRow:
                midPatternLen = 2*i + 1
                print(((b * int((length - (midPatternLen * 3))/2)) +
                       c*midPatternLen +
                       (b * int((length - (midPatternLen * 3))/2))).ljust(length))

            elif i == midRow:
                print(((b * int((length - len(a))/2)) + a +
                       (b * int((length - len(a))/2))).ljust(length))

            elif i > midRow:
                midPatternLen = 2*(width - i - 1) + 1
                print(((b * int((length - (midPatternLen * 3))/2)) +
                       c*midPatternLen +
                       (b * int((length - (midPatternLen * 3))/2))).ljust(length))
