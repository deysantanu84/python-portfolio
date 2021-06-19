# You are given a matrix A which represent operations of size N x 2.
# Assume initially you have a stack-like data structure you have to perform operations on it.
# Operations are of two types:
# 1 x: push an integer x onto the stack and return -1
# 2 0: remove and return the most frequent element in the stack.
# If there is a tie for the most frequent element,
# the element closest to the top of the stack is removed and returned.
# A[i][0] describes the type of operation to be performed.
# A[i][1] describe the element x or 0 corresponding to the operation performed.
# 1 <= N <= 100000
# 1 <= A[i][0] <= 2
# 0 <= A[i][1] <= 10^9
freqMap = {}
setMap = {}
maxFreq = 0


# Function to insert x in the stack
def push(x):
    global maxFreq
    if x not in freqMap:
        freqMap[x] = 0

    freq = freqMap[x] + 1

    freqMap[x] = freq

    if freq > maxFreq:
        maxFreq = freq

    if freq not in setMap:
        setMap[freq] = []

    setMap[freq].append(x)

    return -1


def pop():
    global maxFreq

    top = setMap[maxFreq][-1]
    setMap[maxFreq].pop()

    freqMap[top] -= 1

    if len(setMap[maxFreq]) == 0:
        maxFreq -= 1

    return top


def solve(A):
    global freqMap
    global setMap
    global maxFreq
    freqMap = {}
    setMap = {}
    maxFreq = 0
    result = []
    for entry in A:
        if entry[0] == 1:
            result.append(push(entry[1]))

        elif entry[0] == 2:
            result.append(pop())

    return result


print(solve([[1, 5], [2, 0], [1, 4]]))  # [-1, 5, -1]
print(solve([[1, 5], [1, 7], [1, 5], [1, 7], [1, 4], [1, 5], [2, 0], [2, 0], [2, 0], [2, 0]]))  # [-1, -1, -1, -1, -1, -1, 5, 7, 5, 4]
