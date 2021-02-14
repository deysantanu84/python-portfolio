# https://www.hackerrank.com/challenges/list-comprehensions/problem
# https://www.programiz.com/python-programming/list-comprehension

def listComprehensionExamples():
    # Using for loop
    h_letters = []
    for letter in 'human':
        h_letters.append(letter)
    print('For Loop: %s' % h_letters)

    # Using List comprehension
    h_letters = [letter for letter in 'human']
    print('List Comprehension: %s' % h_letters)

    # Using lambda function
    letters = list(map(lambda p: p, 'human'))
    print('Lambda Function: %s' % letters)

    # Using if condition in list comprehension
    number_list = [k for k in range(20) if k % 2 == 0]
    print('List Comp (if): %s' % number_list)

    # Using nested if condition in list comprehension
    num_list = [q for q in range(100) if q % 2 == 0 if q % 5 == 0]
    print('List Comp (nested if): %s' % num_list)

    # Using if...else in list comprehension
    obj = ["Even" if i % 2 == 0 else "Odd" for i in range(10)]
    print('List Comp (if...else): %s' % obj)

    # Using nested loop in list comprehension
    # Transpose of a matrix using nested loop
    transposed = []
    matrix = [[1, 2, 3, 4], [4, 5, 6, 8]]
    for i in range(len(matrix[0])):
        transposed_row = []
        for row in matrix:
            transposed_row.append(row[i])
        transposed.append(transposed_row)
    print('Transpose of matrix (nested loop): %s' % transposed)

    # Transpose of a matrix using list comprehension
    matrix = [[1, 2], [3, 4], [5, 6], [7, 8]]
    transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    print('Transpose of matrix (list comp): %s' % transpose)


def solution(a, b, c, m):
    return [[g, h, i] for g in range(a + 1) for h in range(b + 1) for i in range(c + 1) if g + h + i != m]


if __name__ == '__main__':
    # listComprehensionExamples()
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print(solution(x, y, z, n))
