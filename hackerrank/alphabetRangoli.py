# https://www.hackerrank.com/challenges/alphabet-rangoli/problem
def print_rangoli(size):
    for i in range(1, size+1):
        print(('-' * int((size - i) * 2)), end='')
        for item1 in range(i):
            letter = chr(ord('a') + (size-item1))
            print(letter + '-', end='')
        for item2 in range(i - 1):
            print((chr(ord('a') + item2)) + '-', end='')
        print(('-' * int((size - i) * 2)).ljust(((size - 1) * 4) + 1))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
