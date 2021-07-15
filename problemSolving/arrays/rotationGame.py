# You are given an integer T (Number of test cases).
# For each test case, you are given an integer array A and an integer B.
# You have to print the same array after rotating it B times towards right.
# NOTE: You can use extra memory.
# First line of the input contains a single integer T.
# Next, each of the test case consists of 2 lines:
# First line begins with an integer |A| denoting the length of array,
# and then |A| integers denote the array elements.
# Second line contains a single integer B
# For each test case, print an array of integers which is the Bth right rotation of input array A,
# on a separate line.
# https://www.geeksforgeeks.org/python-program-right-rotate-list-n/
def kRotations(A, k, N):
    rotatedList = A[-(k % N):] + A[:-(k % N)]
    # print(*rotatedList)
    for i in rotatedList:
        print(i, end=' ')
    print()


def rotationGame():
    T = int(input())
    for i in range(T):
        array = list(map(int, input().split()))
        rotations = int(input())
        arrayLength = array.pop(0)
        kRotations(array, rotations, arrayLength)


if __name__ == '__main__':
    rotationGame()
