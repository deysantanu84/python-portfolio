# Given a positive integer A, write a program to find the Ath Fibonacci number.
# In a Fibonacci series, each term is the sum of the previous two terms and
# the first two terms of the series are 0 and 1. i.e. f(0) = 0 and f(1) = 1.
# Hence, f(2) = 1, f(3) = 2, f(4) = 3 and so on.
# NOTE: 0th term is 0. 1th term is 1 and so on.
# 0 <= A <= 44
# First and only argument is an integer A.
# Return an integer denoting the Ath Fibonacci number.

# Bottom up (Iterative)
# Optimal solution
def fibonacci(A):
    fibList = [0, 1]

    for index in range(2, A + 1):
        fibList.append(fibList[index - 1] + fibList[index - 2])

    return fibList[A]


# Top down (Recursive)
# Not optimal for A > 35
def fibonacciTD(A):
    fibDict = {0: 0, 1: 1, 2: 1, 3: 2}

    if A in fibDict.keys():
        return fibDict[A]

    fibDict[A] = fibonacciTD(A - 1) + fibonacciTD(A - 2)

    return fibDict[A]


print(fibonacci(4))  # 3
print(fibonacci(6))  # 8
print(fibonacci(44))  # 701408733
print(fibonacciTD(4))  # 3
print(fibonacciTD(6))  # 8
print(fibonacciTD(10))  # 55
print(fibonacciTD(20))  # 6765
print(fibonacciTD(30))  # 832040
print(fibonacciTD(35))  # 9227465
